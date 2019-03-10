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

    def test_occupation_string_representation(self):
        occupation = Occupation.objects.create(
            name=Occupation.WARRIOR,
            module=Occupation.WARRIOR_MODULE,
        )
        self.assertEqual(str(occupation), occupation.name)
