from django.core.management.base import BaseCommand, CommandError
from artifical.data.locations import locations
from artifical.models.location import Location


class Command(BaseCommand):
    help = 'Creates all locations defined in artifical/data/locations.py'

    def handle(self, *args, **options):
        print('Creating locations...')
        self.create_locations()
        print('Locations created.\n')

    def create_locations(self):
        for location in locations:
            self.is_already_created_location(location['name'])
            Location.objects.create(**location)

    def is_already_created_location(self, location_name):
        if Location.objects.filter(name=location_name):
            raise Exception('This location already exists', location_name)