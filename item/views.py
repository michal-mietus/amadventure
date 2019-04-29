from collections import namedtuple
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from item.service import ItemService
from item.serializers import ItemAndItemStatisticSerializer


class ItemGetAPIView(APIView):
    def post(self, request, *args, **kwargs):
        level = request.data['level']
        item = ItemService().create_random_item(level)
        if item:
            combined_data = self.get_serialized_and_combined_data(item)
            return Response(combined_data)
        return Response()

    def get_serialized_and_combined_data(self, item):
        item_statistics = item.itemstatistic_set.all()
        ItemDataPattern = self.get_data_pattern()
        combined_data = ItemDataPattern(
            item=item,
            item_statistics=item_statistics
        )
        serializer = ItemAndItemStatisticSerializer(combined_data)
        return serializer.data

    def get_data_pattern(self):
        Pattern = namedtuple('item_data', (
            'item',
            'item_statistics'
            )
        )
        return Pattern