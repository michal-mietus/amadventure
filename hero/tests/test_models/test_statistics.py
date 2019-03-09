import random
from django.test import TestCase
from .set_ups import UserAndHeroSetUp
from ...models.statistics import Statistic


class TestStatistic(UserAndHeroSetUp):
    def setUp(self):
        self.statistics_names = ['strength', 'agility', 'intelligence']

    def test_statistics_create(self):
        hero = self.create_hero('hero')
        for statistic_name in self.statistics_names:
            points = random.randrange(10)
            Statistic.objects.create(
                name=statistic_name,
                points=points,
                hero=hero,
            )
