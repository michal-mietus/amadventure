from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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


class AbilityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Ability.objects.all()
    serializer_class = serializers.AbilitySerializer


class StatisticViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Statistic.objects.all()
    serializer_class = serializers.StatisticSerializer


class OccupationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Occupation.objects.all()
    serializer_class = serializers.OccupationSerializer

