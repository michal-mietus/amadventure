import random
from django.db import models
from artifical.models.mob import Mob
from general_upgrade.models import Statistic


class FightingMob(models.Model):
    mob = models.ForeignKey(Mob, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=1)

    def __str__(self):
        return 'Fighting mob ' + self.mob.name

    def create_statistics(self):
        statistic_points = self.create_main_statistic()
        # TODO add randomly choosing statistics to create
        for statistic in Statistic.STATISTICS:
            if self.mob.mob_class.main_statistic not in statistic:
                statistic_value = random.randrange(statistic_points)
                FightingMobStatistic.objects.create(
                    mob=self,
                    name=statistic[0],
                    points=statistic_value
                )
                statistic_points -= statistic_value


    def create_main_statistic(self):
        statistic_points = (int(self.level) * 3) + 15
        main_statistic_range = statistic_points - len(Statistic.STATISTICS)
        main_statistic_value = random.randint(main_statistic_range//2, main_statistic_range)
        FightingMobStatistic.objects.create(
            mob=self,
            name=self.mob.mob_class.main_statistic,
            points =main_statistic_value
        )
        statistic_points -= main_statistic_value
        return statistic_points


class FightingMobStatistic(Statistic):
    """Statistics which inheritance from base Statistic class and are assigned to the given mob."""
    mob = models.ForeignKey(FightingMob, on_delete=models.CASCADE)

    def __str__(self):
        return 'Fighting mob statistic ' + self.mob.mob.name
