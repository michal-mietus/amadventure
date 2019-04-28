from django.contrib import admin
from item import models


admin.site.register(models.TemporaryItem)
admin.site.register(models.HeroItem)