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

    def create_warrior_active_ability(self, name, unblock_level):
        return Ability.objects.create(
            name=warrior.abilities[name],
            occupation=self.occupation,
            unblock_level=unblock_level,
            category=Ability.ACTIVE,
            function=name
        )

    def test_ability_is_blocked(self):
        charge_ability = self.create_warrior_active_ability('charge', 0)
        super_charge_ability = self.create_warrior_active_ability('super_charge', 3)

        hero_parent_ability = HeroAbility.objects.create(
            ability=charge_ability,
            parent=None,
            level=2
        )

        hero_child_ability = HeroAbility.objects.create(
            ability=super_charge_ability,
            parent=hero_parent_ability
        )

        self.assertEqual(hero_child_ability.is_blocked(), True)

    def test_ability_is_unblocked(self):
        charge_ability = self.create_warrior_active_ability('charge', 0)
        super_charge_ability = self.create_warrior_active_ability('super_charge', 3)

        hero_parent_ability = HeroAbility.objects.create(
            ability=charge_ability,
            parent=None,
            level=4
        )

        hero_child_ability = HeroAbility.objects.create(
            ability=super_charge_ability,
            parent=hero_parent_ability
        )

        self.assertEqual(hero_child_ability.is_blocked(), False)
