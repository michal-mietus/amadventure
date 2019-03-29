import json
from django.test import TestCase
from django.urls import reverse
from django.core import serializers
from django.core.management import call_command
from django.contrib.auth.models import User
from hero.models.occupation import Occupation
from hero.models.statistic import Statistic
from hero.models.ability import Ability, HeroAbility
from hero_upgrade_system.management.commands.create_abilities import Command as CreateAbilities
from hero_upgrade_system.management.commands.create_occupations import Command as CreateOccupations
from hero.views import AbilitiesUpdateView
from hero.models.hero import Hero


class TestAbilitiesUpdateView(TestCase):
    def setUp(self):
        CreateOccupations().handle()
        self.url = reverse('hero:abilities_update')
        self.user = User.objects.create_user(username='username', password='password')
        self.occupation = Occupation.objects.get(name=Occupation.WARRIOR)
        self.hero = Hero.objects.create(user=self.user, name='hero', occupation=self.occupation)
        self.create_statistics()

    def create_statistics(self):
        statistics = {
            'strength': 5,
            'intelligence': 5,
            'agility': 5,
        }
        for name, points in statistics.items():
            Statistic.objects.create(name=name, points=points, hero=self.hero)

    def abilities_which_can_choose_hero(self):
        return Ability.objects.filter(occupation=self.hero.occupation)

    def test_context(self):
        ability = Ability.objects.create(
            name='pull',
            description='desc',
            occupation=self.occupation,
            parent=None,
            unblock_level=0,
            category=Ability.PASSIVE,
            function='',
        )
        hero_ability = HeroAbility.objects.create(
            ability=ability,
            hero=self.hero,
            parent=None,
        )
        self.client.login(username='username', password='password')
        response = self.client.get(self.url)
        ability_object = {
            "level": hero_ability.level,
            "name": hero_ability.ability.name,
            "description": hero_ability.ability.description,
            "unblock_level": hero_ability.ability.unblock_level,
            "parent": hero_ability.parent
        }
        context = json.loads(response.context['abilities'])
        self.assertEqual(context, [[ability_object]])

    def test_valid_form(self):
        self.create_and_login_user()
        hero = self.get_created_hero_through_view('hero2')
        hero_abilities_before_update = hero.heroability_set.all()
        hero.ability_points = len(hero_abilities_before_update) * 3
        hero.save()

        increase_points = 3
        changed_abilities_data_to_post = self.create_updated_heroability_data_to_post(hero, increase_points)
        response = self.client.post(self.url, data=changed_abilities_data_to_post)

        for hero_ability_before in hero_abilities_before_update:
            updated_hero_ability = HeroAbility.objects.get(hero=hero, ability__name=hero_ability_before.ability.name)
            self.assertEqual((hero_ability_before.level + increase_points), updated_hero_ability.level)
        
    def test_invalid_form(self):
        # check if invalid it should response with context.error
        self.create_and_login_user()
        hero = self.get_created_hero_through_view('hero2')

        hero_abilities_before_update = hero.heroability_set.all()
        hero.ability_points = len(hero_abilities_before_update) * 3
        hero.save()

        increase_points = 5
        changed_abilities_data_to_post = self.create_updated_heroability_data_to_post(hero, increase_points)
        response = self.client.post(self.url, data=changed_abilities_data_to_post)

        for hero_ability_before in hero_abilities_before_update:
            updated_hero_ability = HeroAbility.objects.get(hero=hero, ability__name=hero_ability_before.ability.name)
            self.assertEqual(hero_ability_before.level, updated_hero_ability.level)

    def create_and_login_user(self):
        User.objects.create_user(username='username2', password='password2')
        self.client.login(username='username2', password='password2')

    def get_created_hero_through_view(self, hero_name):
        self.client.post(reverse('hero:hero_create'), {
            'name': hero_name,
            'occupation': Occupation.WARRIOR,
        })
        return  Hero.objects.get(name=hero_name)

    def create_updated_heroability_data_to_post(self, hero, increase_points):
        updated_abilities_data = {}
        for hero_ability in HeroAbility.objects.filter(hero=hero):
            updated_abilities_data[hero_ability.ability.name] = hero_ability.level + increase_points
        return updated_abilities_data
