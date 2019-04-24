from django.db import models
from general_upgrade.models import Statistic
from .location import Location


class MobClass(models.Model):
    """
        MobClass segregates mob by their main statistic. 
        This attribute should be mostly the biggest statistics.
    """

    name = models.CharField(max_length=50)
    main_statistic = models.CharField(max_length=50)

    def __str__(self):
        representation = 'Mob Class ' + self.name.capitalize()
        return representation


class Mob(models.Model):
    """
        Artifical opponents which hero can encounter in given location.
        Difficulty tuples represents for: (name, converter) where:
        converter is a multiplier with which we will calculate mob level
    """
    # choice = (displaying_value, value)
    EASY = (1, 'easy')
    MEDIUM = (1.5, 'medium')
    HARD = (2, 'hard')

    DIFFICULTY = (
        (EASY),
        (MEDIUM),
        (HARD)
    )

    name = models.CharField(max_length=50)
    description = models.TextField()
    mob_class = models.ForeignKey(MobClass, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY)

    def __str__(self):
        representation = 'Mob ' + self.name
        return representation
