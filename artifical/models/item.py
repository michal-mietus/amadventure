from django.db import models
from general_upgrade.models import Statistic
from hero.models.hero import Hero


class Item(models.Model):
    """
      In later phase of development we can include some special activities or
      usages, but for now items only change statistics.
    """
    name = models.CharField(max_length=50)
    description = models.TextField()


class ItemStatistics(Statistic):
    """
      Model statistics may be plus or minus, it will be do operations on hero/mob statistics.
      So in that case we have to rewrite whole Statistic class, because it operates on PositiveIntegerFields
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class HeroItem(Item):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
