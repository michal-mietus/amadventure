from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth.models import User
from ..decorators import deny_access_user_with_hero, hero_required
from hero_upgrade_system.models.occupation import Occupation
from ..models.hero import Hero


class TestDenyAccessUserWithHeroDecorator(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='user',
            password='password',
        )
        self.client.login(username='user', password='password')

    def test_allowed_view_for_user_without_hero(self):
        response = self.client.get(reverse('hero:hero_create'))
        self.assertTemplateUsed(response, 'hero/hero_create.html')

    def test_denied_view_for_user_with_hero(self):
        hero = Hero.objects.create(
            name='hero',
            occupation=self.create_warrior_occupation(),
            user=self.user,
        )
        response = self.client.get(reverse('hero:hero_create'))
        self.assertRedirects(response, reverse('hero:main'))

    def create_warrior_occupation(self):
        return Occupation.objects.create(
            name=Occupation.WARRIOR,
            module=Occupation.WARRIOR_MODULE,
            description=Occupation.WARRIOR_DESCRIPTION,
        )


class TestHeroRequiredDecorator(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='user',
            password='password',
        )
        self.client.login(username='user', password='password')

    def test_invalid_access_for_user_without_hero(self):
        response = self.client.get(reverse('hero:statistics_update'))
        self.assertRedirects(response, reverse('hero:hero_create'))

    def test_valid_access_for_user_with_hero(self):
        hero = Hero.objects.create(
            name='hero',
            occupation=self.create_warrior_occupation(),
            user=self.user,
        )
        response = self.client.get(reverse('hero:statistics_update'))
        self.assertTemplateUsed(response, 'hero/statistics_update.html')

    def create_warrior_occupation(self):
        return Occupation.objects.create(
            name=Occupation.WARRIOR,
            module=Occupation.WARRIOR_MODULE,
            description=Occupation.WARRIOR_DESCRIPTION,
        )
