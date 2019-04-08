from django.test import TestCase
from django.core import management
from artifical.data.mob_classes import mob_classes
from artifical.models.location import Location
from artifical.models import mob


class TestCreateLocationsCommand(TestCase):
    def test_are_locations_created(self):
        management.call_command('create_locations')
        for location_object, location_data in zip(Location.objects.all(), locations):
            self.assertEqual(location_object.name, location_data['name'])

