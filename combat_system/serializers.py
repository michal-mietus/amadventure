from rest_framework import serializers
from combat_system.models import FightingMobStatistic, FightingMob


class FightingMobSerializer(serializers.ModelSerializer):
    class Meta:
        model = FightingMob
        fields = (
          'id', 'mob', 'level',
        )


class FightingMobStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = FightingMobStatistic
        fields = (
            'mob', 'name', 'points'
        )
