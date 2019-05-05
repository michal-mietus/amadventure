import random
from django.db import models
from general_upgrade.models import Statistic




class Item(models.Model):
  ITEMS_IMAGES_LOCATION = 'assets/items/'

  name = models.CharField(max_length=50)
  description = models.TextField()
  rarity = models.CharField(max_length=50)
  image = models.ImageField(upload_to='assets/items')


class MainStatistic(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)


class TemporaryItem(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  level = models.PositiveIntegerField()


class ItemStatistic(Statistic):
  """
    Model statistics may be plus or minus, it will be do operations on hero/mob statistics.
    So in that case we have to rewrite whole Statistic class, because it operates on PositiveIntegerFields
  """
  item = models.ForeignKey(TemporaryItem, on_delete=models.CASCADE)