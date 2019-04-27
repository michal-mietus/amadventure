from artifical.data.items import items
from django.test import TestCase


class TestItemsData(TestCase):
    def test_rarity_keys(self):
        rarities = ['common', 'rare']
        self.assertEqual(list(items['rarity'].keys()), rarities)