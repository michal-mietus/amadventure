from django.db import models
from general_upgrade.models import Statistic
from hero.models.hero import Hero


class ItemGeneral(models.Model):
    """
      In later phase of development we can include some special activities or
      usages, but for now items only change statistics.
    """
    COMMON = 'common'
    RARE = 'rare'
    LEGENDARY = 'legendary'

    RARITY = (
      (COMMON, COMMON),
      (RARE, RARE),
      (LEGENDARY, LEGENDARY)
    )

    name = models.CharField(max_length=50)
    description = models.TextField()
    rarity = models.CharField(max_length=35, choices=RARITY)


class ItemWithStatistics(models.Model):
    item = models.ForeignKey(ItemGeneral, on_delete=models.CASCADE)


class HeroItem(ItemWithStatistics):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)

    def create_statistics(self, mob_level):
      """
        Items should be different and base on something like rarity:
        Common: 0.2 of value,
        Rare: 0.5 
        Legendary: 0.8
        etc.
      """
      pass


class ItemStatistic(Statistic):
    """
      Model statistics may be plus or minus, it will be do operations on hero/mob statistics.
      So in that case we have to rewrite whole Statistic class, because it operates on PositiveIntegerFields
    """
    item = models.ForeignKey(ItemWithStatistics, on_delete=models.CASCADE)