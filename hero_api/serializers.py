from rest_framework import serializers
from django.contrib.auth.models import User
from hero.models.hero import Hero, HeroStatistic
from hero.models.ability import Ability
from hero.models.hero import HeroAbility, BodyPart, HeroItem
from hero.models.occupation import Occupation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = (
            'id', 'name', 'description', 'occupation', 
            'parent', 'unblock_level', 'category',
        )


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ('id', 'name', 'description')


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'occupation', 'user', 'statistic_points', 'ability_points')


class HeroAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroAbility
        fields = ('id', 'level', 'ability', 'parent')


class HeroStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroStatistic
        fields = ('id', 'name', 'points')


class HeroItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroItem
        fields = ('name', 'description', 'level', 'rarity')


class BodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyPart
        fields = ('name', 'item')


class HeroEquipmentSerializer(serializers.Serializer):
    backpack_items = HeroItemSerializer(many=True)
    body_parts_with_items = BodyPartSerializer(many=True)
    

class HeroAllDataSerializer(serializers.Serializer):
    hero = HeroSerializer()
    statistics = HeroStatisticSerializer(many=True)
    abilities = HeroAbilitySerializer(many=True)
    occupation = OccupationSerializer()

