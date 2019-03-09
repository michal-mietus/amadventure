from django.test import TestCase
from ...models.ability import Ability
from ...models.occupation import Occupation
from ...models import abilities


class TestAbility(TestCase):
    def setUp(self):
        self.occupation = Occupation.objects.create(
            name=Occupation.WARRIOR,
        )

    def test_create_ability(self):
        ability = Ability(
            name='charge',
            occupation=self.occupation,
            parent_ability=None,
            unblock_level=0,
            level=1,
            category=Ability.ACTIVE,
        )

        # ability module = what with that?
        # function name = can be a string