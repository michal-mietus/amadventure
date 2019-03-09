from django.test import TestCase
from ...models.occupation import Occupation


class TestOccupation(TestCase):
    def test_create_occupation(self):
        name = Occupation.WARRIOR
        module = Occupation.WARRIOR_MODULE
        Occupation.objects.create(
            name=name,
            module=module,
        )
