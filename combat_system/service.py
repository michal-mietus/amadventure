import random
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from hero.models.hero import Hero
from artifical.models.location import Location
from artifical.models import mob
from combat_system.models import FightingMob


class MobService:
    def __init__(self, request, location_pk):
        self.request = request
        self.location_pk = location_pk

    def get_fighting_mob(self):
        # TODO add more complex opponent choosing system
        mob = self.choose_mob(self.location_pk)
        fighting_mob = self.create_fighting_mob(mob)
        fighting_mob.create_statistics()
        return fighting_mob

    def choose_mob(self, location_pk):
        location = Location.objects.get(pk=location_pk)
        mobs = location.mob_set.all()
        if not mobs:
            raise Exception('No mobs created.')
        return random.choice(mobs)

    def create_fighting_mob(self, mob):
        mob_level = self.get_mob_level(mob)
        fighting_mob = FightingMob.objects.create(
            mob=mob,
            level=mob_level
        )
        return fighting_mob

    def get_mob_level(self, mob):
        #hero = get_object_or_404(Hero, user__pk=self.request.user.pk)
        try:
            hero = Hero.objects.get(user__pk=self.request.user.pk)
        except ObjectDoesNotExist:
            raise Exception('You don\'t have created hero!')
        return hero.level * int(float(mob.difficulty))

    def get_hero(self):
        return Hero.objects.get(user__pk=self.request.user.pk)
