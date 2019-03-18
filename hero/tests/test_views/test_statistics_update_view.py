from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from hero_upgrade_system.models.occupation import Occupation
from hero.models.hero import Hero
from hero_upgrade_system.models.statistics import Statistic
from ...views import StatisticsUpdateView


class TestStatisticsUpdateView(TestCase):
    url = reverse_lazy('hero:statistics_update')
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            password='password',
        )

        self.client = Client()
        self.factory = RequestFactory()
        self.occupation = self.create_occupation()
        self.client.login(username='user', password='password')
        response = self.client.post(reverse('hero:hero_create'), {
            'name': 'hero',
            'user': self.user,
            'occupation': self.occupation
        })
        self.hero = Hero.objects.get(user=self.user)

        self.statistics = {
            'strength': 5,
            'intelligence': 5,
            'agility': 5,
        }

        self.client.login(username='user', password='password')
        self.view = StatisticsUpdateView()
    
    def create_occupation(self):
        return Occupation.objects.create(
            name=Occupation.WARRIOR,
            module=Occupation.WARRIOR_MODULE,
            description=Occupation.WARRIOR_DESCRIPTION
        )

    def create_statistics(self, **attributes):
        for name, points in attributes.items():
            Statistic.objects.create(
                name=name,
                hero=self.hero,
                points=points,
            )

    def test_response_code_is_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'hero/statistics_update.html')

    def test_context(self):
        response = self.client.get(self.url)
        points = self.hero.statistic_points
        self.assertEqual(response.context['points'], points)

    def test_sum_of_points(self):
        points_sum = self.view.sum_all_form_points(self.statistics)
        self.assertEqual(points_sum, 15)

    def test_valid_newly_created_statistics(self):
        self.client.post(self.url, self.statistics)
        for name, points in self.statistics.items():
            statistic = Statistic.objects.get(hero=self.hero, name=name)
            self.assertEqual(statistic.points, points)

    def test_valid_updated_statistics(self):
        self.client.post(self.url, self.statistics)
        self.hero.statistic_points = 15
        self.client.post(self.url, self.statistics)

        for statistic in Statistic.objects.filter(hero=self.hero):
            self.assertEqual(statistic.points, 5)

    def test_valid_sets_new_statistc_points(self):
        self.hero.statistic_points = 5
        self.hero.save()
        self.client.login(username='username', password='password')
        response = self.client.post(self.url, {
            'strength': 8,
            'intelligence': 6,
            'agility': 6,
        })
        self.hero = Hero.objects.get(pk=self.hero.pk)
        self.assertEqual(self.hero.statistic_points, 0)
