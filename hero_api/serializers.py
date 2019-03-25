from rest_framework import serializers
from django.contrib.auth.models import User
from hero.models.hero import Hero
from hero_upgrade_system.models.statistics import Statistic
from hero_upgrade_system.models.ability import Ability, HeroAbility
from hero_upgrade_system.models.occupation import Occupation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'occupation')


class HeroAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroAbility
        fields = ('id', 'level', 'ability', 'parent')
        
        
class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = (
            'id', 'name', 'description', 'occupation', 
            'parent', 'unblock_level', 'category',
        )

class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ('id', 'name', 'points')


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ('id', 'name', 'description')
