from django.contrib import admin
from hero.models.occupation import Occupation
from .models.ability import Ability, HeroAbility
from hero.models.statistic import Statistic


admin.site.register(Occupation)
admin.site.register(Ability)
admin.site.register(HeroAbility)
admin.site.register(Statistic)
