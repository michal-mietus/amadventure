from django.db import models
from .hero import Hero


class Statistic(models.Model):
    STATISTICS = (
        ('strength', 'strength'),
        ('agility', 'agility'),
        ('intelligence', 'intelligence'),
    )
    name = models.CharField(max_length=35, choices=STATISTICS) # how does it works in view/form ?
    points = models.PositiveIntegerField()
    hero = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
    )
