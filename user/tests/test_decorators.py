from django.test import TestCase, Client, RequestFactory
from django.shortcuts import reverse
from django.contrib.auth.models import User
from ..decorators import deny_logged_user_access


class TestDenyLoggedUserAccessDecorator(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='user',
            password='password',
        )
        self.sign_up_url = reverse('user:sign_up')

    def test_logged_user_redirected(self):
        self.client.login(
            username='user',
            password='password'
        )
        response = self.client.get(self.sign_up_url)
        self.assertRedirects(response, reverse('hero:main'))

    def test_logged_user_allowed_view(self):
        response = self.client.get(self.sign_up_url)
        self.assertTemplateUsed(response, 'user/sign_up.html')
