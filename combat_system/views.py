from django.shortcuts import render
from rest_framework import viewsets
from .models import FightingMob
from .serializers import FightingMobSerializer


class FightingMobViewSet(viewsets.ModelViewSet):
    queryset = FightingMob.objects.all()
    serializer_class = FightingMobSerializer
