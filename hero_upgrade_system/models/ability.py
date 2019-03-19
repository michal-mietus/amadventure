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
    description = models.TextField()
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
        if self.parent:
            if self.parent.level >= self.ability.unblock_level:
                return False
        return True

    def get_parent_ability(self):
        return self.ability.parent

    def get_all_descendants(self):
        """Get all descendants of HeroAbility object. (childs of childs...)"""
        descendants = []
        childs = self.heroability_set.all()
        for child in childs:
            descendants.append(child)
            child_descendants = child.get_all_descendants()
            if child_descendants:
                descendants.extend(child_descendants)
        if descendants:
            return descendants
        return []

    def get_core_abilities(self):
        core_abilities = []
        for hero_ability in HeroAbility.objects.filter(hero=self.hero):
            if hero_ability.parent == None:
                print(hero_ability)
                core_abilities.append(hero_ability)
        return core_abilities

