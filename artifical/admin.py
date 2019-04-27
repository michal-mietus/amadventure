from django.contrib import admin
from artifical import models


admin.site.register(models.location.Location)
admin.site.register(models.mob.Mob)
admin.site.register(models.mob.MobClass)
admin.site.register(models.item.TemporaryItem)
admin.site.register(models.item.HeroItem)
