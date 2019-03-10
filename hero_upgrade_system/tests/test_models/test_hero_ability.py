from django.test import TestCase
from ...models.ability import Ability, HeroAbility
from ...models.occupation import Occupation
from ...models.occupations import warrior


class TestHeroAbility(TestCase):
    def setUp(self):
        self.occupation = Occupation.objects.create(
            name=Occupation.WARRIOR,
            module=Occupation.WARRIOR_MODULE,
        )

        self.ability = Ability.objects.create(
            name=warrior.abilities['charge'],
            occupation=self.occupation,
            unblock_level=0,
            category=Ability.ACTIVE,
            function='charge'
        )

        self.hero_parent_ability = HeroAbility.objects.create(
            ability=self.ability,
            parent=None
        )

        self.hero_ability = HeroAbility.objects.create(
            ability=self.ability,
            parent=self.hero_parent_ability
        )

    def test(self):
        pass