from django.core.management.base import BaseCommand, CommandError
from artifical.data.mob_classes import mob_classes
from artifical.models.mob import MobClass


class Command(BaseCommand):
    help = 'Creates all mob classes'

    def handle(self, *args, **options):
        print('Creating mob classess...')
        self.create_mob_classes()
        print('Mob classes created.\n')

    def create_mob_classes(self):
        for mob_class in mob_classes:
            MobClass.objects.create(
                name=mob_class['name'],
                main_statistic=mob_class['main_statistic']
            )