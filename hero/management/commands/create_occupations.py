from django.core.management.base import BaseCommand, CommandError
from hero.models.occupation import Occupation
from hero.models import occupations


class Command(BaseCommand):
    help = 'Creates base Abilities objects in database.'

    def handle(self, *args, **options):
        print('Creating occupations...')
        self.create_occupation(Occupation.WARRIOR, Occupation.WARRIOR_MODULE)
        self.create_occupation(Occupation.MAGE, Occupation.MAGE_MODULE)
        self.create_occupation(Occupation.THIEF, Occupation.THIEF_MODULE)
        print('Occupations created.\n')
        
    def create_occupation(self, name, module):
        if Occupation.objects.filter(name=name):
            raise Exception('This occupations already exists', name)
        Occupation.objects.create(
            name=name,
            module=module
        )

