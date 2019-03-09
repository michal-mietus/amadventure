from django.db import models


class Occupation(models.Model):
    WARRIOR = 'warrior'
    THIEF = 'thief'
    MAGE = 'mage'

    # TODO occupation name and module should be related!
    # now I can choose different module to different name

    OCCUPATIONS = (
        (WARRIOR, 'Warrior'),
        (THIEF, 'Thief'),
        (MAGE, 'Mage')
    )

    MODULES = (
        (WARRIOR, 'hero_upgrade_system.models.abilities.warrior'),
        (MAGE, 'hero_upgrade_system.models.abilities.mage'),
        (THIEF, 'hero_upgrade_system.models.abilities.thief'),
    )

    name = models.CharField(max_length=35, choices=OCCUPATIONS)
    module = models.CharField(max_length=100, choices=MODULES)

    def __str__(self):
        return self.name
