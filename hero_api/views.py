from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from hero_api import serializers
from hero.models.hero import Hero, HeroStatistic
from hero.models.ability import Ability
from hero.models.hero import HeroAbility
from hero.models.occupation import Occupation


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


class HeroStatisticViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = HeroStatistic.objects.all()
    serializer_class = serializers.HeroStatisticSerializer

    def list(self, request, *args, **kwargs):
        hero = get_object_or_404(Hero, pk=kwargs['hero_pk'])
        queryset = hero.herostatistic_set.all()
        serializer = serializers.HeroStatisticSerializer(queryset, many=True)
        return Response(serializer.data)


class OccupationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Occupation.objects.all()
    serializer_class = serializers.OccupationSerializer
