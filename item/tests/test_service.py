from django.test import TestCase
from item.service import ItemService
from item.models import TemporaryItem, ItemStatistic
from general_upgrade.models import Statistic


class TestItemService(TestCase):
    def setUp(self):
        self.service = ItemService()

    def test_get_statistic_points_top_scope_valid(self):
        top_points_scope = self.service._ItemService__get_statistic_points_top_scope()
        statistics_number = len(Statistic.STATISTICS)
        self.assertEqual(top_points_scope, 1 / statistics_number)

    def test_create_statistic_valid(self):
        item = TemporaryItem.objects.create(
            name='item',
            description='description',
            level=5,
            rarity='common'
        )
        self.service._ItemService__create_statistic('strength', item)
        self.assertEqual(len(item.itemstatistic_set.all()), 1)

    def test_create_random_item(self):
        item = self.service.create_random_item(5)

    def test_create_item_with_given_rarity(self):
        rarity = 'common'
        item = self.service.create_random_item_with_rarity(5, rarity)
        self.assertEqual(item.rarity['name'], rarity)

    def test_create_item_with_given_rarity_have_statistics(self):
        rarity = 'common'
        item = self.service.create_random_item_with_rarity(5, rarity)
        self.assertEqual(len(item.itemstatistic_set.all()), len(Statistic.STATISTICS))

    def test_create_item_with_given_name(self):
        name = 'sword'
        item = self.service.create_item_with_name(5, name)
    
    def test_create_item_with_given_name_have_statistics(self):
        name = 'sword'
        item = self.service.create_item_with_name(5, name)
        self.assertEqual(len(item.itemstatistic_set.all()), len(Statistic.STATISTICS))