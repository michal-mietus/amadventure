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
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    unblock_level = models.PositiveIntegerField()
    category = models.CharField(max_length=35, choices=CATEGORIES)
    function = models.CharField(max_length=100) # occupation.module.function

    def __str__(self):
        return self.name


class HeroAbility(models.Model):
    level = models.PositiveIntegerField(default=0)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def is_blocked(self):
        """Parent level must be equal or bigger than unblock level."""
        if self.parent.level >= self.ability.unblock_level:
            return False
        return True
