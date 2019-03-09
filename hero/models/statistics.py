from django.db import models
from .hero import Hero


class Statistic(models.Model):
    # object = MyModel(name=MyModel.STRENGTH)
    STRENGTH = 'strength'
    AGILITY = 'agility'
    INTELLIGENCE = 'intelligence'

    NAME_CHOICES = (
        (STRENGTH, 'strength'),
        (AGILITY, 'agility'),
        (INTELLIGENCE, 'intelligence'),
    )
    name = models.CharField(max_length=35, choices=NAME_CHOICES) # how does it works in view/form ?
    points = models.PositiveIntegerField()
    hero = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
    )
