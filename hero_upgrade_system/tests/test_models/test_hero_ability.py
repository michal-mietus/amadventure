from django.test import TestCase
from django.contrib.auth.models import User
from hero.models.hero import Hero
from ...models.ability import Ability, HeroAbility
from ...models.occupation import Occupation
from ...models.occupations import warrior


class TestHeroAbility(TestCase):
    def setUp(self):
        self.occupation = Occupation.objects.create(
            name=Occupation.WARRIOR,
            module=Occupation.WARRIOR_MODULE,
        )

        self.user = User.objects.create_user(
            username='username',
            password='password',
        )

        self.hero = Hero.objects.create(
            name='hero',
            user=self.user,
            occupation=self.occupation,
        )

        self.ability = Ability.objects.create(
            name=warrior.abilities['charge'],
            occupation=self.occupation,
            unblock_level=0,
            category=Ability.ACTIVE,
            function='charge'
        )

        self.hero_parent_ability = HeroAbility.objects.create(
            hero=self.hero,
            ability=self.ability,
            parent=None
        )

        self.hero_ability = HeroAbility.objects.create(
            hero=self.hero,
            ability=self.create_warrior_active_ability('super_charge', 3),
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
            hero=self.hero,
            ability=charge_ability,
            parent=None,
            level=2
        )

        hero_child_ability = HeroAbility.objects.create(
            hero=self.hero,
            ability=super_charge_ability,
            parent=hero_parent_ability
        )

        self.assertEqual(hero_child_ability.is_blocked(), True)

    def test_ability_is_unblocked(self):
        charge_ability = self.create_warrior_active_ability('charge', 0)
        super_charge_ability = self.create_warrior_active_ability('super_charge', 3)

        hero_parent_ability = HeroAbility.objects.create(
            hero=self.hero,
            ability=charge_ability,
            parent=None,
            level=4
        )

        hero_child_ability = HeroAbility.objects.create(
            hero=self.hero,
            ability=super_charge_ability,
            parent=hero_parent_ability
        )

        self.assertEqual(hero_child_ability.is_blocked(), False)

    def test_get_parent_ability(self):
        parent_ability = Ability.objects.create(
            name='charge',
            occupation=self.occupation,
            parent=None,
            unblock_level=0,
            category=Ability.ACTIVE,
            function='charge',
        )

        hero_parent_ability = HeroAbility.objects.create(
            hero=self.hero, 
            ability=parent_ability,
            parent=None
        )

        child_ability = Ability.objects.create(
            name='super_charge',
            occupation=self.occupation,
            parent=parent_ability,
            unblock_level=3,
            category=Ability.ACTIVE,
            function='super_charge',
        )

        hero_child_ability = HeroAbility.objects.create(
            hero=self.hero, 
            ability=child_ability,
            parent=hero_parent_ability
        )

        ability = hero_child_ability.get_parent_ability()
        self.assertEqual(ability, hero_parent_ability.ability)
