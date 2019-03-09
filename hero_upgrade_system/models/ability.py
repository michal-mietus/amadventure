from django.db import models
from .occupation import Occupation


class Ability(models.Model):
    PASSIVE = 'passive'
    ACTIVE = 'active'
    CATEGORIES = (
        (PASSIVE, 'passive'),
        (ACTIVE, 'active'),
    )

    name = models.CharField(max_length=35)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    parent_ability = models.ForeignKey('self', on_delete=models.CASCADE)
    level = models.PositiveIntegerField()
    unblock_level = models.PositiveIntegerField()
    category = models.CharField(max_length=35, choices=CATEGORIES)
    ability_function = models.CharField(max_length=100) # occupation.module.function
    
    def is_blocked(self):
        """Parent level must be equal or bigger than unblock level."""
        if parent.level >= unblock_level:
            return False
        return True
