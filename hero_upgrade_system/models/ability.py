from django.db import models
from hero.models.hero import Hero
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
    # probably can be deleted, but have to name functions just as Ability
    function = models.CharField(max_length=100) # occupation.module.function

    def __str__(self):
        return self.name


class HeroAbility(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        string_representation = self.hero.name + ' ' + self.ability.name
        return string_representation
        

    def is_blocked(self):
        """Parent level must be equal or bigger than unblock level."""
        if self.parent.level >= self.ability.unblock_level:
            return False
        return True

    def get_parent(self):
        parent_ability = self.ability.parent
        return HeroAbility.objects.get(ability=parent_ability)