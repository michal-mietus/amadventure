from django.db import models


class Statistic(models.Model):
    STRENGTH = 'strength'
    AGILITY = 'agility'
    INTELLIGENCE = 'intelligence'
    HEALTH = 'health'

    STATISTICS = (
        (STRENGTH, STRENGTH),
        (AGILITY, AGILITY),
        (INTELLIGENCE, INTELLIGENCE),
        (HEALTH, HEALTH),
    )

    name = models.CharField(max_length=35, choices=STATISTICS)
    points = models.PositiveIntegerField(default=5)

    def __str__(self):
        representation = 'Statistic ' + self.name.capitalize()
        return representation
