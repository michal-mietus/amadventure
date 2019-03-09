from django.db import models
from .hero import Hero


class Statistic(models.Model):
    name = models.CharField(max_length=35)
    points = models.PositiveIntegerField()
    hero = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
    )
