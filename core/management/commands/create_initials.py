from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from artifical.data.locations import locations
from artifical.models.location import Location


class Command(BaseCommand):
    help = 'Run all initializing commands.'

    def handle(self, *args, **options):
        artifical_commands = ['create_locations', 'create_mob_classes', 'create_mobs']
        hero_commands = ['create_occupations', 'create_abilities']
        for command in artifical_commands + hero_commands:
            call_command(command)
