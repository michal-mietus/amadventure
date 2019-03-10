from django.core.management.base import BaseCommand, CommandError
from hero_upgrade_system.models.ability import Ability
from hero_upgrade_system.models.occupation import Occupation
from hero_upgrade_system.models import occupations


class Command(BaseCommand):
    help = 'Creates base Abilities objects in database.'
    OCCUPATIONS = [
        (Occupation.WARRIOR, occupations.warrior),
        (Occupation.MAGE, occupations.mage),
        (Occupation.THIEF, occupations.thief),
    ]

    def handle(self, *args, **options):
        self.create_all_abilities()

    def create_all_abilities(self):
        for occupation_pair in self.OCCUPATIONS:
            self.create_abilities_in_occupation(
                occupation_name=occupation_pair[0],
                module=occupation_pair[1],
            )

    def create_abilities_in_occupation(self, occupation_name, module):
        occupation = Occupation.objects.get(name=occupation_name) # Occupation.WARRIOR etc.
        abilities = module.abilities
        for ability in abilities:
            ability = abilities[ability]
            parent = ability['parent']
            if parent:
                parent = self.get_parent_or_delete_duplicates(parent)
                del ability['parent'] # when unpacking, collids with parent object

                Ability.objects.create(
                    occupation=occupation,
                    parent=parent,
                    **ability
                )
            else: 
                Ability.objects.create(
                    occupation=occupation,
                    **ability
                )

    def get_parent_or_delete_duplicates(self, name):
        try:
            return Ability.objects.get(name=name)
        except Exception as e:
            abilities = Ability.objects.all()
            ability = abilities[0]
            self.delete_duplicates(Ability.objects.all()[1:])
            return ability

    def delete_duplicates(self, abilities):
        for ability in abilities:
            Ability.objects.filter(pk=ability.pk).delete()