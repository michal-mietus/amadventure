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
from hero.models import occupations
from hero.models.occupation import Occupation
from hero.models.statistic import Statistic
from hero.models.ability import Ability, HeroAbility
from .decorators import deny_access_user_with_hero, hero_required
from .models.hero import Hero
from .forms import HeroCreateForm, StatisticsChangeForm, AbilitiesChangeForm


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

        self.create_new_hero_abilities(hero)
        self.create_statistics(hero)

        return super().form_valid(form)

    def create_new_hero_abilities(self, hero):
        """Callled when user is creating hero. """
        self.create_core_abilities(hero)
        self.create_descendant_abilities(hero)

    def create_core_abilities(self, hero):
        for ability in hero.occupation.get_core_abilities():
            HeroAbility.objects.create(
                hero=hero,
                ability=ability,
                parent=None,
            )

    def create_descendant_abilities(self, hero):
        for ability in hero.occupation.get_descendant_abilities():
            parent = HeroAbility.objects.get(ability=ability.parent)
            HeroAbility.objects.create(
                hero=hero,
                ability=ability,
                parent=parent,
            )


    def create_statistics(self, hero):
        """ If hero doesn't have created statistics. """
        for name in Statistic.STATISTICS:
            Statistic.objects.create(
                name=name[0],
                hero=hero,
            )

    def if_have_parent_return(self, ability, hero):
        if ability.parent is not None:
            self.get_hero_ability_parent(ability, hero)
        return None

    def get_hero_ability_parent(self, ability, hero):
        return HeroAbility.objects.filter(ability__name=ability.parent.name, hero=hero)

    def get_current_user(self):
        return User.objects.get(pk=self.request.user.pk)
    

# TODO Hero required or redirect to create hero
@method_decorator([login_required, hero_required], name='dispatch')
class StatisticsUpdateView(FormView):
    form_class = StatisticsChangeForm
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
        for statistic in self.get_current_hero().statistic_set.all():
            fields_names_and_min_values[statistic.name] = statistic.points
        return fields_names_and_min_values

    def get_initial(self):
        initial = super().get_initial()
        for statistic in Statistic.objects.filter(hero=self.get_current_hero()):
            initial[statistic.name] = statistic.points
        return initial

    def get_current_hero(self):
        return Hero.objects.get(user=self.get_current_user())

    def get_current_user(self):
        return User.objects.get(pk=self.request.user.pk)

    def form_valid(self, form):
        statistics = {
            'strength': form.cleaned_data['strength'],
            'intelligence': form.cleaned_data['intelligence'],
            'agility': form.cleaned_data['agility'],
        }
        hero = self.get_current_hero()
        all_hero_points = hero.sum_all_statistic_points()
        form_sum_statistics = self.sum_all_form_points(statistics)

        points_sum_invalid_error = self.is_points_sum_invalid(all_hero_points, form_sum_statistics)
        lower_points_error = self.are_points_lower_than_they_were(form)
        if points_sum_invalid_error or lower_points_error:
            errors = []
            if points_sum_invalid_error:
                errors.append(points_sum_invalid_error)
            if lower_points_error:
                errors.append(lower_points_error)
            return render(self.request, self.template_name, {
                'form': form,
                'errors': errors,
            })
        self.set_new_hero_statistics_points(all_hero_points, form_sum_statistics)
        self.update_statistics(statistics)

        return super().form_valid(form)

    def sum_all_form_points(self, statistics):
        form_points_sum = 0
        for points in statistics.values():
            form_points_sum += points
        return form_points_sum

    def is_points_sum_invalid(self, all_hero_points, form_sum_statistics):
        """ Sum of points already assigned to statistics and 
            free points should be same. 
            """
        if all_hero_points < form_sum_statistics:
            return 'Amount of upgraded points is not correct.'

    def are_points_lower_than_they_were(self, form):
        for hero_statistic in self.get_current_hero().statistic_set.all():
            if form.cleaned_data[hero_statistic.name] < hero_statistic.points:
                return "You can't set your statistic points lower than they was."
    
    def set_new_hero_statistics_points(self, hero_points, form_points):
        hero = self.get_current_hero()
        hero.statistic_points = hero_points - form_points
        hero.save()

    def update_statistics(self, statistics):
        for name, points in statistics.items():
            statistic = Statistic.objects.get(hero=self.get_current_hero(), name=name)
            statistic.points = points
            statistic.save()


# TODO Hero required or redirect to create hero
@method_decorator([login_required, hero_required], name='dispatch')
class AbilitiesUpdateView(FormView):
    form_class = AbilitiesChangeForm
    template_name = 'hero/abilities_update.html'
    success_url = reverse_lazy('hero:main')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'fields_names_and_min_values': self.get_fields_names_and_min_values()
        })
        return kwargs
    
    def get_fields_names_and_min_values(self):
        hero = self.get_current_hero()
        abilities = HeroAbility.objects.filter(hero=hero)
        names_and_min_values = {}
        for hero_ability in abilities:
            names_and_min_values[hero_ability.ability.name] = hero_ability.level
        return names_and_min_values

    def get_hero_occupation(self):
        return self.get_current_hero().occupation

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
