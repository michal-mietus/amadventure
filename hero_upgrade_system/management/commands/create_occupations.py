from django.core.management.base import BaseCommand, CommandError
from hero_upgrade_system.models.occupation import Occupation
from hero_upgrade_system.models import occupations


class Command(BaseCommand):
    help = 'Creates base Abilities objects in database.'

    def handle(self, *args, **options):
        self.create_occupation(Occupation.WARRIOR, Occupation.WARRIOR_MODULE)
        self.create_occupation(Occupation.MAGE, Occupation.MAGE_MODULE)
        self.create_occupation(Occupation.THIEF, Occupation.THIEF_MODULE)
        
    def create_occupation(self, name, module):
        Occupation.objects.create(
            name=name,
            module=module
        )

