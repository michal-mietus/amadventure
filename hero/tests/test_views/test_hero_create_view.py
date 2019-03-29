from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from hero.models.occupation import Occupation
from hero.models.ability import Ability
from hero.models.hero import Hero
from ...views import HeroCreateView


class TestCreateHeroView(TestCase):
    url = reverse_lazy('hero:hero_create')
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            password='password',
        )
        self.client = Client()
        self.factory = RequestFactory()
        self.create_occupation()
    
    def create_occupation(self):
        Occupation.objects.create(
            name=Occupation.WARRIOR,
            module=Occupation.WARRIOR_MODULE,
            description=Occupation.WARRIOR_DESCRIPTION
        )

    def test_valid_form(self):
        self.client.login(username='user', password='password')
        response = self.client.post(self.url, {
            'name': 'hero',
            'occupation': Occupation.WARRIOR
        })
        hero = Hero.objects.get(user=self.user)
        self.assertEqual(hero.name, 'hero') 
        self.assertRedirects(response, reverse('hero:statistics_update'))

    def test_response_code_is_200(self):
        self.client.login(username='user', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        self.client.login(username='user', password='password')
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'hero/hero_create.html')

    def test_hero_created_new_abilities(self):
        self.client.login(username='user', password='password')
        response = self.client.post(self.url, {
            'name': 'hero',
            'occupation': Occupation.WARRIOR
        })
        hero = Hero.objects.get(user=self.user)
        self.assertEqual(len(hero.heroability_set.all()), len(Ability.objects.all()))

    def test_create_descendant_abilities(self):
        occupation = Occupation.objects.get(
            name=Occupation.WARRIOR
        )
        hero = Hero.objects.create(
            user=self.user,
            name='hero',
            occupation=occupation,
        )
        view = HeroCreateView()
        view.create_descendant_abilities(hero)

    def test_create_hero_post_data(self):
        self.client.login(username='user', password='password')
        response = self.client.post(self.url, {
            'name': 'hero',
            'occupation': Occupation.WARRIOR
        })
