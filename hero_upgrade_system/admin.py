from django.contrib import admin
from .models.occupation import Occupation
from .models.ability import Ability, HeroAbility
from .models.statistics import Statistic


admin.site.register(Occupation)
admin.site.register(Ability)
admin.site.register(HeroAbility)
admin.site.register(Statistic)
