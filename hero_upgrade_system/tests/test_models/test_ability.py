from django.test import TestCase
from ...models.ability import Ability
from ...models.occupation import Occupation
from ...models import occupations


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
            category=Ability.ACTIVE,
        )

    def test_str_representation(self):
        name = 'str'
        ability = self.create_ability(name, 10)
        self.assertEqual(str(ability), name)
