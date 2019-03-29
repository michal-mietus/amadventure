from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from hero_api import serializers
from hero.models.hero import Hero
from hero_upgrade_system.models.statistics import Statistic
from hero_upgrade_system.models.ability import Ability, HeroAbility
from hero_upgrade_system.models.occupation import Occupation


class HeroViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Hero.objects.all().order_by('name')
    serializer_class = serializers.HeroSerializer


class HeroAbilityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = HeroAbility.objects.all()
    serializer_class = serializers.HeroAbilitySerializer

    def list(self, request, *args, **kwargs):
        hero = get_object_or_404(Hero, pk=kwargs['hero_pk'])
        queryset = hero.heroability_set.all()
        serializer = serializers.HeroAbilitySerializer(queryset, many=True)
        return Response(serializer.data)


class AbilityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Ability.objects.all()
    serializer_class = serializers.AbilitySerializer


class StatisticViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Statistic.objects.all()
    serializer_class = serializers.StatisticSerializer

    def list(self, request, *args, **kwargs):
        hero = get_object_or_404(Hero, pk=kwargs['hero_pk'])
        queryset = hero.statistic_set.all()
        serializer = serializers.StatisticSerializer(queryset, many=True)
        return Response(serializer.data)


class OccupationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Occupation.objects.all()
    serializer_class = serializers.OccupationSerializer
