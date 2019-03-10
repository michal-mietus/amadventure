from django.db import models


class Occupation(models.Model):
    WARRIOR = 'warrior'
    THIEF = 'thief'
    MAGE = 'mage'

    # TODO occupation name and module should be related!
    # now I can choose different module for different name

    OCCUPATIONS = (
        (WARRIOR, 'Warrior'),
        (THIEF, 'Thief'),
        (MAGE, 'Mage')
    )

    # TODO create separate class for this data ?

    WARRIOR_MODULE = 'hero_upgrade_system.models.abilities.warrior'
    MAGE_MODULE = 'hero_upgrade_system.models.abilities.mage'
    THIEF_MODULE = 'hero_upgrade_system.models.abilities.thief'

    MODULES = (
        (WARRIOR, WARRIOR_MODULE),
        (MAGE, MAGE_MODULE),
        (THIEF, THIEF_MODULE),
    )

    name = models.CharField(max_length=35, choices=OCCUPATIONS)
    module = models.CharField(max_length=100, choices=MODULES)

    def __str__(self):
        return self.name
