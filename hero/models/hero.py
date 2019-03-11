from django.db import models
from django.contrib.auth.models import User
from hero_upgrade_system.models.occupation import Occupation


class Hero(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=35)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)

    def __str__(self):
        return 'Hero ' + self.name 

    ## skills = upgrade_sys.upgrade__skills.all (or one to one?)

    def get_all_stats(self):
        return self.statistic_set.all()

    def upgrade_stats(self, **stats):
        statistics = self.get_all_stats()
        for statistic in statistics:
            statistic.points += stats[statistic.name]
            statistic.save()
            pass
