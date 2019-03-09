from django.db import models
from django.contrib.auth.models import User
from .statistics import Statistic


class Hero(models.Model):
    owner = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=35)
    stats = models.ForeignKey(
        Statistic,
        on_delete=models.CASCADE,
    )
    ## skills = upgrade_sys.upgrade__skills.all (or one to one?)
