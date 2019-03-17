from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core import serializers
from hero_upgrade_system.models import occupations
from hero_upgrade_system.models.occupation import Occupation
from hero_upgrade_system.models.statistics import Statistic
from hero_upgrade_system.models.ability import Ability, HeroAbility
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
        for ability in Ability.objects.filter(occupation=hero.occupation):
            parent_ability = self.if_have_parent_return(ability, hero)
            HeroAbility.objects.create(
                hero=hero,
                ability=ability,
                parent=parent_ability,
            )

    def create_statistics(self, hero):
        """ If hero doesn't have created statistics. """
        statistics = ['strength', 'intelligence', 'agility']
        for name in statistics:
            Statistic.objects.create(
                name=name,
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

        if self.is_points_sum_invalid(all_hero_points, form_sum_statistics):
            error = 'Amount of upgraded points is not correct.'
            return render(self.request, self.template_name, {
                'form': form,
                'error': error,
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
            return True
    
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
            'fields_names': self.get_fields_names()
        })
        return kwargs
    
    def get_fields_names(self):
        occupation_name = self.get_hero_occupation().name
        abilities = Ability.objects.filter(occupation__name=occupation_name)
        names = []
        for ability in abilities:
            names.append(ability.name)
        return names

    def get_hero_occupation(self):
        return Occupation.objects.get(pk=self.get_current_hero().occupation.pk)

    def get_initial(self):
        initial = super().get_initial()
        for hero_ability in self.get_hero_abilities():
            initial[hero_ability.ability.name] = hero_ability.level
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        abilities = serializers.serialize('json', self.get_hero_abilities())
        context['points'] = self.get_current_hero().ability_points
        context['abilities'] = abilities
        return context

    def form_valid(self, form):
        if self.is_points_sum_invalid(form):
            error = 'Amount of upgraded levels is not correct.'
            return render(self.request, self.template_name, {
                'form': form,
                'error': error,
            })
        self.update_hero_abilities(form)
        return super().form_valid(form)

    def is_points_sum_invalid(self, form):
        if self.sum_form_points(form) > self.get_current_hero().sum_all_ability_points():
            return True
        return False
    
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
