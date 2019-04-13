from collections import namedtuple
from rest_framework import serializers
from hero_api.serializers import HeroSerializer, HeroAbilitySerializer, HeroStatisticSerializer, AbilitySerializer
from combat_system.serializers import FightingMobSerializer, FightingMobStatisticSerializer
from artifical.models.location import Location
from artifical.models.item import Item
from artifical.models.mob import Mob


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id', 'name', 'description',
        )


class MobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mob
        fields = (
            'name', 'description', 'mob_class', 'location', 'difficulty'
        )


class CombatDataSerializer(serializers.Serializer):
    hero = HeroSerializer()
    hero_statistics = HeroStatisticSerializer(many=True)
    hero_abilities = HeroAbilitySerializer(many=True)
    abilities = AbilitySerializer(many=True)
    fighting_mob_statistics = FightingMobStatisticSerializer(many=True)
    fighting_mob = FightingMobSerializer()
    mob = MobSerializer()