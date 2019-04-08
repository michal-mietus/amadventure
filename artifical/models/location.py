from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()

    def __str__(self):
        return self.name.capitalize()
