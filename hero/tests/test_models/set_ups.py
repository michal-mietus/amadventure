from django.test import TestCase
from django.contrib.auth.models import User
from ...models.hero import Hero


class UserAndHeroSetUp(TestCase):
    def create_user(self):
        user = User.objects.create(
            username='username',
            password='password'
        )
        return user

    def create_hero(self, name):
        user = self.create_user()
        hero = Hero.objects.create(
            user=user,
            name=name,
        )
        return hero