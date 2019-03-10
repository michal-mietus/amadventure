from django.test import TestCase
from ...models.ability import Ability
from ...models.occupation import Occupation
from ...models import abilities


class TestAbility(TestCase):
    def setUp(self):
        self.occupation = Occupation.objects.create(
            name=Occupation.WARRIOR,
            module=Occupation.WARRIOR_MODULE,
        )

    def create_ability(self, name, level):
        ability = Ability.objects.create(
            name=name,
            occupation=self.occupation,
            parent=None,
            unblock_level=0,
            level=level,
            category=Ability.ACTIVE,
            function='charge',
        )
        return ability

    def test_create_ability(self):
        ability = Ability.objects.create(
            name='charge',
            occupation=self.occupation,
            parent=None,
            unblock_level=0,
            level=1,
            category=Ability.ACTIVE,
        )

        # ability module = what with that?
        # function name = can be a string

    def test_ablity_is_blocked(self):
        """Parent ability level is lower than child unlock level"""
        parent_ability = self.create_ability('charge', 2)
        child_ability = Ability.objects.create(
            name='super charge',
            occupation=self.occupation,
            parent=parent_ability,
            unblock_level=3,
            level=0,
            category=Ability.ACTIVE
        )
        self.assertEqual(child_ability.is_blocked(), True)

    def test_ablity_is_unblocked(self):
        """Parent ability level is equal to child unlock level"""
        parent_ability = self.create_ability('charge', 3)
        child_ability = Ability.objects.create(
            name='super charge',
            occupation=self.occupation,
            parent=parent_ability,
            unblock_level=3,
            level=0,
            category=Ability.ACTIVE
        )
        self.assertEqual(child_ability.is_blocked(), False)