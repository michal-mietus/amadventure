from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render
from hero_upgrade_system.models import occupations
from hero_upgrade_system.models.occupation import Occupation
from hero_upgrade_system.models.statistics import Statistic
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
        Hero.objects.create(
            user=user,
            name=form.cleaned_data['name'],
            occupation=occupation,
        )
        return super().form_valid(form)

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
        self.are_sums_of_points_equal(statistics)
        self.if_hero_have_statistics_update_other_create(statistics)

        return super().form_valid(form)

    def are_sums_of_points_equal(self, statistics):
        """ Sum of points already assigned to statistics and 
            free points should be same. 
            For now, user have to use all of his free points to upgrade
            at one time.
            """

        hero = self.get_current_hero()
        if hero.sum_all_statistic_points() != self.sum_all_form_points(statistics):
            error = 'Amount of upgraded points is not correct.'
            return render(self.request, self.template_name, context= {
                'error': error,
            })
    
    def sum_all_form_points(self, statistics):
        form_points_sum = 0
        for statistic in statistics.values():
            form_points_sum += statistic
        return form_points_sum

    def if_hero_have_statistics_update_other_create(self, statistics):
        hero_statistics = Statistic.objects.filter(hero=self.get_current_hero())
        if not hero_statistics:
            self.create_statistics(statistics)
        else:
            self.update_statistics(statistics)

    def create_statistics(self, statistics):
        """ If hero doesn't have created statistics. """
        hero = self.get_current_hero()
        for name, points in statistics.items():
            Statistic.objects.create(
                name=name,
                points=points,
                hero=hero,
            )

    def update_statistics(self, statistics):
        for name, points in statistics.items():
            statistic = Statistic.objects.get(hero=self.get_current_hero(), name=name)
            statistic.points += points
            statistic.save()


# TODO Hero required or redirect to create hero
@method_decorator(login_required, name='dispatch')
class AbilitiesUpdateView(FormView):
    form_class = AbilitiesChangeForm
    template_name = 'hero/abilities_update.html'
    success_url = 'hero/main.html'

    def get_occupation_with_abilities(self):
        warrior_abilities = occupations.warrior.abilities
        thief_abilities = occupations.thief.abilities
        mage_abilities = occupations.mage.abilities

        return [warrior_abilities, thief_abilities, mage_abilities]
