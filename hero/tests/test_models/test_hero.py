from django.test import TestCase
from .set_ups import UserAndHeroSetUp
from ...models.hero import Hero


class TestHero(UserAndHeroSetUp):
    def test_hero_string_representation(self):
        hero_name = 'hero'
        occupation = self.create_occupation()
        hero = self.create_hero(
            hero_name
        )
        self.assertEqual(str(hero), 'Hero ' + hero_name)
