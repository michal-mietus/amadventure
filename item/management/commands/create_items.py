from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from item.models import Item, MainStatistic
from item.data.items import items


class Command(BaseCommand):
    help = 'Creates all item defined in item/data/items.py'

    def handle(self, *args, **options):
        print('Creating items...')
        self.create_items()
        print('Items created.\n')

    def create_items(self):
        for rarity, items_list in items['rarity'].items():
            for item in items_list:
                item_object = Item(
                    name=item['name'],
                    description=item['description'],
                    rarity=rarity,
                )
                image_path = Item.ITEMS_IMAGES_LOCATION + item['image']
                item_object.image = image_path
                item_object.save()
                self.create_item_main_statistics(item, item_object)

    def create_item_main_statistics(self, item_data, item_as_object):
        for statistic in item_data['statistics']:
            MainStatistic.objects.create(
                item=item_as_object,
                name=statistic
            )

    def is_already_created_item(self, name):
        if Item.objects.filter(name=name):
            raise Exception('This item already exists', name)