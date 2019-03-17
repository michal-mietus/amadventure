from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from hero_upgrade_system.models.occupation import Occupation


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

    def sum_all_ability_points(self):
        points_sum = self.ability_points
        for ability in self.heroability_set.all():
            points_sum += ability.level
        return points_sum
