from django.test import TestCase
from django.contrib.auth.models import User
from hero.models.hero import Hero
from hero.models.occupation import Occupation
from hero.models.statistic import Statistic


class TestStatistic(TestCase):

    def create_user(self, username):
        return User.objects.create(
            username=username,
            password='zaq1@WSX'
        )

    def create_hero(self):
        return Hero.objects.create(
            user=self.create_user('user1'),
            name='hero1',
            occupation=self.create_occupation()
        )

    def create_occupation(self):
        return Occupation.objects.create(
            name=Occupation.WARRIOR,
            module=Occupation.WARRIOR_MODULE,
        )

    def test_create_statistic_object(self):
        Statistic.objects.create(
            name=Statistic.STRENGTH,
            points=1,
            hero=self.create_hero()
        )