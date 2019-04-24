from collections import namedtuple
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from hero_api import serializers
from hero.models.hero import Hero, HeroStatistic
from hero.models.ability import Ability
from hero.models.hero import HeroAbility
from hero.models.occupation import Occupation


class HeroCreateView(APIView):
    http_method_names = ['post', 'head']

    def post(self, request):
        request.data['user'] = request.user.pk
        serializer = serializers.HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            hero = Hero.objects.get(user__pk=request.user.pk)
            hero.create_all_initials()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeroViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Hero.objects.all().order_by('name')
    serializer_class = serializers.HeroSerializer


class HeroAllDataViewSet(viewsets.ViewSet):
    def list(self, request):
        hero = get_object_or_404(Hero, user__pk=request.user.pk)
        HeroDataPattern = namedtuple('hero_data', ('hero', 'statistics', 'abilities', 'occupation'))
        hero_data = HeroDataPattern(
            hero=hero,
            statistics=hero.herostatistic_set.all(),
            abilities=hero.heroability_set.all(),
            occupation=hero.occupation,
        )
        serializer = serializers.HeroAllDataSerializer(hero_data)
        return Response(serializer.data)


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


class OccupationAbilityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Ability.objects.all()
    serializer_class = serializers.AbilitySerializer

    def list(self, request, *args, **kwargs):
        occupation = get_object_or_404(Occupation, pk=kwargs['occupation_pk'])
        queryset = occupation.ability_set.all()
        serializer = serializers.AbilitySerializer(queryset, many=True)
        return Response(serializer.data)


class HeroStatisticViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = HeroStatistic.objects.all()
    serializer_class = serializers.HeroStatisticSerializer

    def list(self, request, *args, **kwargs):
        hero = get_object_or_404(Hero, pk=kwargs['hero_pk'])
        queryset = hero.herostatistic_set.all()
        serializer = serializers.HeroStatisticSerializer(queryset, many=True)
        return Response(serializer.data)

class HeroStatisticAllUpgrade(APIView):
    http_method_names = ['post', 'head']

    def post(self, request):
        hero = Hero.objects.get(user__pk=request.user.pk)
        passed_serializers = []
        for statistic in request.data['statistics']:
            statistic_object = hero.herostatistic_set.get(pk=statistic['id'])
            serializer = serializers.HeroStatisticSerializer(
                instance=statistic_object,
                data=statistic,
            )
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            passed_serializers.append(serializer)

        for serializer in passed_serializers:
            serializer.save()

        hero.statistic_points = request.data['heroStatisticPoints']
        hero.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HeroAbilityAllUpgrade(APIView):
    http_method_names = ['post', 'head']

    def post(self, request):
        hero = Hero.objects.get(user__pk=request.user.pk)
        passed_serializers = []
        print(request.data)
        for ability in request.data['abilities']:
            heroability_object = hero.heroability_set.get(pk=ability['id'])
            serializer = serializers.HeroAbilitySerializer(
                instance=heroability_object,
                data=ability,
            )
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            passed_serializers.append(serializer)

        for serializer in passed_serializers:
            serializer.save()
        
        hero.ability_points = request.data['heroAbilityPoints']
        hero.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OccupationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Occupation.objects.all()
    serializer_class = serializers.OccupationSerializer
