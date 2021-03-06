import json
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core import serializers
from .models import occupations
from .models.occupation import Occupation
from .models.ability import Ability
from .models.hero import Hero, HeroAbility, HeroStatistic
from .decorators import deny_access_user_with_hero, hero_required
from .forms import HeroCreateForm, HeroStatisticsChangeForm, AbilitiesChangeForm


class MainView(TemplateView):
    template_name = 'hero/main.html'


@method_decorator([login_required, deny_access_user_with_hero], name='dispatch')
class HeroCreateView(FormView):
    form_class = HeroCreateForm
    template_name = 'hero/hero_create.html'
    success_url = reverse_lazy('hero:statistics_update')

    def form_valid(self, form):
        user = self.get_current_user()
        occupation = Occupation.objects.get(name=form.cleaned_data['occupation'])
        hero = Hero.objects.create(
            user=user,
            name=form.cleaned_data['name'],
            occupation=occupation,
        )

        hero.create_all_initials()
        return super().form_valid(form)

    def get_current_user(self):
        return User.objects.get(pk=self.request.user.pk)
    

# TODO Hero required or redirect to create hero
@method_decorator([login_required, hero_required], name='dispatch')
class HeroStatisticsUpdateView(FormView):
    form_class = HeroStatisticsChangeForm
    template_name = 'hero/statistics_update.html'
    success_url = reverse_lazy('hero:abilities_update')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['points'] = self.get_current_hero().statistic_points
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['fields_names_and_min_values'] = self.get_fields_names_and_min_values()
        return kwargs

    def get_fields_names_and_min_values(self):
        fields_names_and_min_values = {}
        for statistic in self.get_current_hero().herostatistic_set.all():
            fields_names_and_min_values[statistic.name] = statistic.points
        return fields_names_and_min_values

    def get_initial(self):
        initial = super().get_initial()
        for statistic in HeroStatistic.objects.filter(hero=self.get_current_hero()):
            initial[statistic.name] = statistic.points
        return initial

    def get_current_hero(self):
        return Hero.objects.get(user=self.get_current_user())

    def get_current_user(self):
        return User.objects.get(pk=self.request.user.pk)

    def form_valid(self, form):
        hero = self.get_current_hero()
        errors = self.get_errors(form)
        if errors:
            return render(self.request, self.template_name, {
                'form': form,
                'errors': errors,
            })

        hero.update_statistics(form)
        return super().form_valid(form)

    def get_errors(self, form):
        # create list of validators and iterate through them,
        # dont call every validator separately
        errors = []
        if self.are_points_lower_than_they_were(form):
            errors.append(self.are_points_lower_than_they_were(form))
        return errors

    def are_points_lower_than_they_were(self, form):
        for hero_statistic in self.get_current_hero().herostatistic_set.all():
            if form.cleaned_data[hero_statistic.name] < hero_statistic.points:
                return "You can't set your statistic points lower than it was."


# TODO Hero required or redirect to create hero
@method_decorator([login_required, hero_required], name='dispatch')
class AbilitiesUpdateView(FormView):
    form_class = AbilitiesChangeForm
    template_name = 'hero/abilities_update.html'
    success_url = reverse_lazy('hero:main')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'fields_names_and_min_values': self.get_current_hero().get_heroability_names_with_levels_dict()
        })
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        for hero_ability in self.get_hero_abilities():
            initial[hero_ability.ability.name] = hero_ability.level
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        abilities = self.get_all_required_ability_data()
        context['points'] = json.dumps(self.get_current_hero().ability_points)
        context['abilities'] = json.dumps(abilities)
        return context
    
    def get_abilities_grouped_by_core_abilities(self):
        try:
            random_ability = self.get_current_hero().heroability_set.all()[0]
        except Exception as e:
            print('No abilities set.')
        grouped_abilities = []
        core_abilities = random_ability.get_core_abilities()
        for core_ability in core_abilities:
            ability_branch = [core_ability]
            ability_branch.extend(core_ability.get_all_descendants())
            grouped_abilities.append(ability_branch)
        return grouped_abilities

    def get_all_required_ability_data(self):
        grouped_abilities = self.get_abilities_grouped_by_core_abilities()
        abilities_data_to_send = []
        for branch in grouped_abilities:
            serialized_branch = []
            for ability in branch:
                ability_object = {
                    'level': ability.level,
                    'name': ability.ability.name,
                    'description': ability.ability.description,
                    'unblock_level': ability.ability.unblock_level,
                }
                parent = ability.parent
                if parent:
                    ability_object.update(parent=parent.ability.name)
                else:
                    ability_object.update(parent=None)
                serialized_branch.append(ability_object)
            abilities_data_to_send.append(serialized_branch)
        return abilities_data_to_send

    def form_valid(self, form):
        lower_abilities_error = self.are_points_lower_than_they_were(form)
        points_sum_invalid_error = self.is_points_sum_invalid(form)
        if lower_abilities_error or points_sum_invalid_error:
            errors = []
            if lower_abilities_error:
                errors.append(lower_abilities_error)
            if points_sum_invalid_error:
                errors.append(points_sum_invalid_error)
            return render(self.request, self.template_name, {
                'form': form,
                'errors': errors,
            })
        self.update_hero_abilities(form)
        return super().form_valid(form)

    def are_points_lower_than_they_were(self, form):
        for hero_ability in self.get_current_hero().heroability_set.all():
            if form.cleaned_data[hero_ability.ability.name] < hero_ability.level:
                return "You can't set your abilities level lower than they was."

    def is_points_sum_invalid(self, form):
        if self.sum_form_points(form) > self.get_current_hero().sum_all_ability_points():
            return 'Amount of upgraded levels is not correct.'
    
    def sum_form_points(self, form):
        points_sum = 0
        for level in form.cleaned_data.values():
            points_sum += level
        return points_sum

    def update_hero_abilities(self, form):
        self.calculate_new_hero_ability_points(form)

        for changed_field_name, level in form.cleaned_data.items():
            # one problem, we're updating even don't changed levels
            hero_ability = self.get_hero_ability(changed_field_name)
            hero_ability.level = level
            hero_ability.save()
    
    def calculate_new_hero_ability_points(self, form):
        hero = self.get_current_hero()
        hero.ability_points = hero.sum_all_ability_points() - self.sum_form_points(form)
        hero.save()

    def get_hero_ability(self, name):
        return HeroAbility.objects.get(hero=self.get_current_hero(), ability__name=name)

    def get_hero_abilities(self):
        return HeroAbility.objects.filter(hero=self.get_current_hero())

    def get_current_hero(self):
        return Hero.objects.get(user=self.get_current_user())

    def get_current_user(self):
        return User.objects.get(pk=self.request.user.pk)
