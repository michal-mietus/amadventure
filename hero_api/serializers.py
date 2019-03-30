from rest_framework import serializers
from django.contrib.auth.models import User
from hero.models.hero import Hero, HeroStatistic
from hero.models.ability import Ability
from hero.models.hero import HeroAbility
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
        fields = ('name', 'occupation', 'user')


class HeroAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroAbility
        fields = ('id', 'level', 'ability', 'parent')


class HeroStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroStatistic
        fields = ('id', 'name', 'points')


class HeroAllDataSerializer(serializers.Serializer):
    hero = HeroSerializer()
    statistics = HeroStatisticSerializer(many=True)
    abilities = HeroAbilitySerializer(many=True)
    occupation = OccupationSerializer()

