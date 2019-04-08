from django.core.management.base import BaseCommand, CommandError
from artifical.data.mobs import mobs
from artifical.models.mob import Mob
from artifical.models.mob import MobClass
from artifical.models.location import Location


class Command(BaseCommand):
    help = 'Creates all mobs defined in artifical/data/mobs.py'

    def handle(self, *args, **options):
        print('Creating mobs...')
        self.create_mobs()
        print('Mobs created.\n')

    def create_mobs(self):
        for mob in mobs:
            self.is_already_created_mob(mob['name'])
            mob['mob_class'] = MobClass.objects.get(name=mob['mob_class'])
            mob['location'] = Location.objects.get(name=mob['location'])
            mob['difficulty'] = mob['difficulty'][0]
            Mob.objects.create(**mob)

    def is_already_created_mob(self, mob_name):
        if Mob.objects.filter(name=mob_name):
            raise Exception('This mob already exists', mob_name)