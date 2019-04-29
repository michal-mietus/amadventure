import json
import requests
from collections import namedtuple
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from combat_system.service import MobService
from hero_api.serializers import HeroStatisticSerializer, HeroAbilitySerializer
from hero.models.hero import Hero
from artifical.models.location import Location
from artifical import serializers


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer


class ExpeditionView(APIView):
    # TODO don't use post method, request should be done when user select location and approve fight desire
    def get(self, request, *args, **kwargs):
        location_id = kwargs['location_id']
        
        return Response(self.get_serialized_data(request, location_id))
    
    def get_serialized_data(self, request, location_id):
        mob_service = MobService(request, location_id)
        fighting_mob = mob_service.get_fighting_mob()
        fighting_mob_statistics = fighting_mob.fightingmobstatistic_set.all()
        mob = fighting_mob.mob

        hero = Hero.objects.get(user__pk=self.request.user.pk)
        hero_abilities = hero.get_unblocked_abilities()
        hero_statistics = hero.herostatistic_set.all()

        abilities = [ability.ability for ability in hero_abilities]

        CombatDataPattern = self.create_object_pattern()
        data_as_object = CombatDataPattern(
            hero=hero,
            mob=mob,
            abilities=abilities,
            hero_abilities=hero_abilities,
            hero_statistics=hero_statistics,
            fighting_mob=fighting_mob,
            fighting_mob_statistics=fighting_mob_statistics,
        )
        serializer = serializers.CombatDataSerializer(data_as_object)
        return serializer.data

    def create_object_pattern(self, **kwargs):
        CombatDataPattern = namedtuple('combat_data', (
            'hero',
            'mob',
            'abilities',
            'fighting_mob',
            'fighting_mob_statistics',
            'hero_abilities', 
            'hero_statistics',)
        )
        return CombatDataPattern
