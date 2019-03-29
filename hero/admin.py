from django.contrib import admin
from .models.hero import Hero
from hero.models.occupation import Occupation
from hero.models.ability import Ability, HeroAbility
from hero.models.statistic import Statistic


admin.site.register(Hero)
admin.site.register(Occupation)
admin.site.register(Ability)
admin.site.register(HeroAbility)
admin.site.register(Statistic)
