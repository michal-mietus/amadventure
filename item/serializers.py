from rest_framework import serializers
from item.models import TemporaryItem, Item, ItemStatistic


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class TemporaryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryItem
        fields = '__all__'


class ItemStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemStatistic
        fields = ('pk', 'name', 'points', 'item')


class ItemAndItemStatisticSerializer(serializers.Serializer):
    item = TemporaryItemSerializer()
    item_statistics = ItemStatisticSerializer(many=True)