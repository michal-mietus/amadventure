import random
from django.db import models
from general_upgrade.models import Statistic
from hero.models.hero import Hero


class TemporaryItem(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField()
  level = models.PositiveIntegerField()
  rarity = models.CharField(max_length=50)


class HeroItem(models.Model):
  item = models.ForeignKey(TemporaryItem, on_delete=models.CASCADE)
  hero = models.ForeignKey(Hero, on_delete=models.CASCADE)


class ItemStatistic(Statistic):
  """
    Model statistics may be plus or minus, it will be do operations on hero/mob statistics.
    So in that case we have to rewrite whole Statistic class, because it operates on PositiveIntegerFields
  """
  item = models.ForeignKey(TemporaryItem, on_delete=models.CASCADE)