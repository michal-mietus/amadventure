from django.db import models
from hero.models.hero import Hero


class Statistic(models.Model):
    STRENGTH = 'strength'
    AGILITY = 'agility'
    INTELLIGENCE = 'intelligence'

    STATISTICS = (
        (STRENGTH, STRENGTH),
        (AGILITY, AGILITY),
        (INTELLIGENCE, INTELLIGENCE),
    )

    name = models.CharField(max_length=35, choices=STATISTICS)
    points = models.PositiveIntegerField()
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
