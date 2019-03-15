from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from hero_upgrade_system.models.occupation import Occupation
from hero_upgrade_system.models.statistics import Statistic
from hero.models.hero import Ability
from hero.views import AbilitiesUpdateView
from hero.models.hero import Hero


class TestAbilitiesChangeView(TestCase):
    def setUp(self):
        self.url = reverse('hero:abilities_update')
        self.user = User.objects.create_user(username='username', password='password')
        self.occupation = Occupation.objects.create(
            name=Occupation.WARRIOR,
            module=Occupation.WARRIOR_MODULE,
            description=Occupation.WARRIOR_DESCRIPTION,
        )
        self.hero = Hero.objects.create(user=self.user, name='hero', occupation=self.occupation)
        self.create_statistics()

    def create_statistics(self):
        statistics = {
            'strength': 5,
            'intelligence': 5,
            'agility': 5,
        }
        for name, points in statistics.items():
            Statistic.objects.create(name=name, points=points, hero=self.hero)

    def abilities_which_can_choose_hero(self):
        return Ability.objects.filter(occupation=self.hero.occupation)

    def test_context(self):
        response = self.client.get(self.url)
        self.assertQuerysetEqual(response.context, self.abilities_which_can_choose_hero())

    def test_valid_form(self):
        pass
