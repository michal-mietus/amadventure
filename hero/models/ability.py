from django.db import models
from hero.models.occupation import Occupation


class Ability(models.Model):
    PASSIVE = 'passive'
    ACTIVE = 'active'
    CATEGORIES = (
        (PASSIVE, 'passive'),
        (ACTIVE, 'active'),
    )

    name = models.CharField(max_length=35)
    description = models.TextField()
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    unblock_level = models.PositiveIntegerField()
    category = models.CharField(max_length=35, choices=CATEGORIES)
    # probably can be deleted, but have to name functions just as Ability
    function = models.CharField(max_length=100) # occupation.module.function

    def __str__(self):
        return self.name
