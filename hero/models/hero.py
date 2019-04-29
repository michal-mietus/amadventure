from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from general_upgrade.models import Statistic
from item.models import TemporaryItem
from hero.models.occupation import Occupation
from hero.models.ability import Ability


LEVEL_UP = {
    'STATISTIC_POINTS': 3,
    'ABILITY_POINTS': 1,
}


class Hero(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=35)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)
    statistic_points = models.PositiveIntegerField(default=15)
    # discrepancy of naming (in ability its Level)
    ability_points = models.PositiveIntegerField(default=3)

    def __str__(self):
        return 'Hero ' + self.name 

    ## skills = upgrade_sys.upgrade__skills.all (or one to one?)

    def add_experience(self, experience):
        self.experience += experience
        if self.experience >= self.get_experience_to_level_up():
            self.level_up()
        self.save()

    def level_up(self):
            self.experience -= self.get_experience_to_level_up()
            self.level += 1
            self.statistic_points += LEVEL_UP['STATISTIC_POINTS']
            self.ability_points += LEVEL_UP['ABILITY_POINTS']

    def get_experience_to_level_up(self):
        return self.level * 100

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

    def create_all_initials(self):
        """
            Method to call all methods which have to be initialized
            when hero is first time created.
        """
        self.create_initial_statistics()
        self.create_initial_core_abilities()
        self.create_initial_descendant_abilities()

    def create_initial_statistics(self):
        for statistic in HeroStatistic.STATISTICS:
            HeroStatistic.objects.create(
                name=statistic[0],
                hero=self,
            )

    def create_initial_core_abilities(self):
        for ability in self.occupation.get_core_abilities():
            HeroAbility.objects.create(
                hero=self,
                ability=ability,
                parent=None,
            )

    def create_initial_descendant_abilities(self):
        for ability in self.occupation.get_descendant_abilities():
            parent_hero_ability = HeroAbility.objects.get(ability=ability.parent)
            HeroAbility.objects.create(
                hero=self,
                ability=ability,
                parent=parent_hero_ability,
            )

    def update_statistics(self, statistics_form):
        if self.is_form_valid(statistics_form):
            self.update_statistic_points(statistics_form)
            for statistic_name, statistic_points in statistics_form.cleaned_data.items():
                hero_statistic = self.herostatistic_set.get(name=statistic_name)
                hero_statistic.points = statistic_points
                hero_statistic.save()

    def is_form_valid(self, statistics_form):
        if self.get_hero_statistics_free_points(statistics_form) >= 0:
            return True
        return False 

    def sum_statistics_points(self):
        points_sum = 0
        for statistic in self.herostatistic_set.all():
            points_sum += statistic.points
        return points_sum

    def sum_statistic_form_points(self, statistics_form):
        points_sum = 0
        for statistic_name, statistic_points in statistics_form.cleaned_data.items():
            points_sum += statistic_points
        return points_sum

    def get_hero_statistics_free_points(self, statistics_form):
        free_statistics_points = self.sum_all_statistic_points() - self.sum_statistic_form_points(statistics_form)
        return free_statistics_points

    def update_statistic_points(self, statistics_form):
        self.statistic_points = self.get_hero_statistics_free_points(statistics_form)
        self.save()

    def get_heroability_names_with_levels_dict(self):
        names_and_levels = {}
        for hero_ability in self.heroability_set.all():
            names_and_levels[hero_ability.ability.name] = hero_ability.level
        return names_and_levels
    
    def get_unblocked_abilities(self):
        hero_abilities = []
        for ability in self.heroability_set.all():
            if not ability.is_blocked():
                hero_abilities.append(ability)
        return hero_abilities


class HeroItem(TemporaryItem):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)


class BodyPart(models.Model):
    HEAD = 'head'
    NECK = 'neck'
    CHEST = 'chest'
    LEFT_ARM = 'left_arm'
    RIGHT_ARM = 'right_arm'
    LEGS = 'legs'

    BODY_PARTS = (
        (HEAD, HEAD),
        (NECK, NECK),
        (CHEST, CHEST),
        (LEFT_ARM, LEFT_ARM),
        (RIGHT_ARM, RIGHT_ARM),
        (LEGS, LEGS)
    )

    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, choices=BODY_PARTS)
    item = models.ForeignKey(HeroItem, on_delete=models.CASCADE, null=True)


@receiver(post_save, sender=Hero)
def create_body_parts(sender, instance, **kwargs):
    for (body_part_name, _) in BodyPart.BODY_PARTS:
        BodyPart.objects.create(
            name=body_part_name,
            hero=instance,
        )


class HeroAbility(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        string_representation = self.hero.name + ' ' + self.ability.name.capitalize()
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


class HeroStatistic(Statistic):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
