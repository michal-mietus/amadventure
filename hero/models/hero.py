from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from hero.models.occupation import Occupation
from hero.models.ability import Ability


class Hero(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=35)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    statistic_points = models.PositiveIntegerField(default=15)
    # discrepancy of naming (in ability its Level)
    ability_points = models.PositiveIntegerField(default=3)

    def __str__(self):
        return 'Hero ' + self.name 

    ## skills = upgrade_sys.upgrade__skills.all (or one to one?)

    def get_all_stats(self):
        return self.herostatistic_set.all()

    def upgrade_statistics(self, **stats):
        statistics = self.get_all_stats()
        for statistic in statistics:
            statistic.points += stats[statistic.name]
            statistic.save()

    def sum_all_statistic_points(self):
        """ It's used to validation, did user send back stats upgraded
            only with free points that he had. """
        points_sum = self.statistic_points
        for statistic in self.herostatistic_set.all():
            points_sum += statistic.points
        return points_sum

    def sum_all_ability_points(self):
        points_sum = self.ability_points
        for ability in self.heroability_set.all():
            points_sum += ability.level
        return points_sum


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


class HeroStatistic(models.Model):
    STRENGTH = 'strength'
    AGILITY = 'agility'
    INTELLIGENCE = 'intelligence'

    STATISTICS = (
        (STRENGTH, STRENGTH),
        (AGILITY, AGILITY),
        (INTELLIGENCE, INTELLIGENCE),
    )

    name = models.CharField(max_length=35, choices=STATISTICS)
    points = models.PositiveIntegerField(default=5)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
