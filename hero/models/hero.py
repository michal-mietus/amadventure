from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from hero_upgrade_system.models.occupation import Occupation
from hero_upgrade_system.models.ability import Ability


class Hero(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=35)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    statistic_points = models.PositiveIntegerField(default=15)
    ability_points = models.PositiveIntegerField(default=3)

    def __str__(self):
        return 'Hero ' + self.name 

    ## skills = upgrade_sys.upgrade__skills.all (or one to one?)

    def get_all_stats(self):
        return self.statistic_set.all()

    def upgrade_statistics(self, **stats):
        statistics = self.get_all_stats()
        for statistic in statistics:
            statistic.points += stats[statistic.name]
            statistic.save()

    def sum_all_statistic_points(self):
        """ It's used to validation, did user send back stats upgraded
            only with free points that he had. """
        points_sum = self.statistic_points
        for statistic in self.statistic_set.all():
            points_sum += statistic.points
        return points_sum

    def create_new_hero_abilities(self):
        """Callled when user is creating hero. """
        hero_occupation = self.occupation
        for ability in self.get_all_occuppation_abilities():
            parent_ability = self.get_hero_ability_parent(ability)
            HeroAbility.objects.create(
                hero=hero,
                ability=ability,
                parent=parent_ability,
            )
        
    def get_all_occuppation_abilities(self):
        return Ability.objects.filter(occupation=self.occupation)

    def get_hero_ability_parent(self, ability):
        return HeroAbility.objects.get(name=ability.parent.name, hero=self)
