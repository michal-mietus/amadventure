from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from hero_upgrade_system.models import occupations
from hero_upgrade_system.models.occupation import Occupation
from .decorators import deny_access_user_with_hero
from .models.hero import Hero
from .forms import HeroCreateForm


class MainView(TemplateView):
    template_name = 'hero/main.html'


@method_decorator([login_required, deny_access_user_with_hero], name='dispatch')
class HeroCreateView(FormView):
    form_class = HeroCreateForm
    template_name = 'hero/hero_create.html'
    success_url = reverse_lazy('hero:statistics_change')

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
    

class StatisticsChangeView(FormView):
    pass


# Hero required
@method_decorator(login_required, name='dispatch')
class AbilitiesChangeView(FormView):
    def get_occupation_with_abilities(self):
        warrior_abilities = occupations.warrior.abilities
        thief_abilities = occupations.thief.abilities
        mage_abilities = occupations.mage.abilities

        return [warrior_abilities, thief_abilities, mage_abilities]
