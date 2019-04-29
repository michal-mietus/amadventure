import random
from django.db import models
from general_upgrade.models import Statistic


class TemporaryItem(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField()
  level = models.PositiveIntegerField()
  rarity = models.CharField(max_length=50)


class ItemStatistic(Statistic):
  """
    Model statistics may be plus or minus, it will be do operations on hero/mob statistics.
    So in that case we have to rewrite whole Statistic class, because it operates on PositiveIntegerFields
  """
  item = models.ForeignKey(TemporaryItem, on_delete=models.CASCADE)