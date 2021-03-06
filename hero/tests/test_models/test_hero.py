from django.test import TestCase
from .set_ups import UserAndHeroSetUp
from hero.models.hero import HeroStatistic
from ...models.hero import Hero


class TestHero(UserAndHeroSetUp):
    def setUp(self):
        super().setUp()
        self.hero_name = 'hero'
        self.hero = self.create_hero('hero')

    def test_hero_string_representation(self):
        self.assertEqual(str(self.hero), 'Hero ' + self.hero_name)

    def test_get_all_stats(self):
        self.assertQuerysetEqual(self.hero.get_all_stats(), self.hero.herostatistic_set.all())

    def test_upgrade_statistics(self):
        statistics = {
            'strength': 5,
            'intelligence': 5,
            'agility': 5,
        }
        self.create_hero_statistics(statistics)
        self.hero.upgrade_statistics(**statistics)

        for name, points in statistics.items():
            self.assertEqual(points*2, self.hero.herostatistic_set.get(name=name).points)

    def create_hero_statistics(self, statistics):
        for name, points in statistics.items():
            HeroStatistic.objects.create(
                name=name, 
                points=points,
                hero=self.hero
            )
