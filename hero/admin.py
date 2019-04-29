from django.contrib import admin
from .models.hero import Hero
from hero.models.occupation import Occupation
from hero.models.ability import Ability
from hero.models.hero import HeroAbility, HeroStatistic, HeroItem


admin.site.register(Hero)
admin.site.register(Occupation)
admin.site.register(Ability)
admin.site.register(HeroAbility)
admin.site.register(HeroStatistic)
admin.site.register(HeroItem)
