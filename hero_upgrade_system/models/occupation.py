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

    WARRIOR_MODULE = 'hero_upgrade_system.models.occupations.warrior'
    MAGE_MODULE = 'hero_upgrade_system.models.occupations.mage'
    THIEF_MODULE = 'hero_upgrade_system.models.occupations.thief'

    MODULES = (
        (WARRIOR_MODULE, WARRIOR_MODULE),
        (MAGE_MODULE, MAGE_MODULE),
        (THIEF_MODULE, THIEF_MODULE),
    )

    WARRIOR_DESCRIPTION = 'Warrior is ...'
    MAGE_DESCRIPTION = 'Mage is ...'
    THIEF_DESCRIPTION = 'Thief is ...'

    DESCRIPTIONS = (
        (WARRIOR_DESCRIPTION, WARRIOR_DESCRIPTION),
        (MAGE_DESCRIPTION, MAGE_DESCRIPTION),
        (THIEF_DESCRIPTION, THIEF_DESCRIPTION),
    )

    name = models.CharField(max_length=35, choices=OCCUPATIONS)
    module = models.CharField(max_length=100, choices=MODULES)
    description = models.TextField()

    # usage module
    # __import__(module)
    # vars(module.models.occupations.<occupation>)[function_name] 
    # don't know why import only main app folder.

    def __str__(self):
        return self.name
