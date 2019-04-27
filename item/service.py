import random
from hero.models.hero import Hero
from general_upgrade.models import Statistic
from artifical.models import mob, location
from item.models import  TemporaryItem, ItemStatistic
from item.data.items import items, RARITIES


class ItemService:

    @staticmethod
    def __get_multipliers():
        multipliers_dictionary = {}
        multiplier = 2
        for name in RARITIES.keys():
            multipliers_dictionary[name] = multiplier
            multiplier += 1
        return multipliers_dictionary
        
    RARITY_MULTIPLIERS = __get_multipliers.__func__()

    def __init__(self):
        self.item = None

    def create_item_with_name(self, level, name):
        item = self.get_item(name)
        created_item = self.__create_item_and_statistics(item, level)
        return created_item
        
    def get_item(self, name):
        for rarity in items['rarity'].keys():
            for item_dictionary in items['rarity'][rarity]:
                if item_dictionary['name'] == name:
                    return item_dictionary

    def create_random_item(self, level):
        """
            If rarity returns None, then item isn't created
        """
        rarity = self.__draw_rarity()
        if rarity:
            created_item = self.__create_item(level, rarity)
            return created_item

    def create_random_item_with_rarity(self, level, rarity):
        created_item = self.__create_item(level, rarity)
        return created_item

    def __create_item(self, level, rarity):
        item = random.choice(items['rarity'][rarity])
        created_item = self.__create_item_and_statistics(item, level)    
        return created_item

    def __draw_rarity(self):
        # add method to randoomly create item, but to be sure 
        # that it is created
        drawn_number = random.randint(0, 100) / 100
        for rarity in RARITIES.keys():
            if drawn_number <= RARITIES[rarity]['chance']:
                return RARITIES[rarity]['name']
        return None

    def __create_item_and_statistics(self, item, level):
        created_item = TemporaryItem.objects.create(
            name=item['name'],
            description=item['description'],
            level=level,
            rarity=item['rarity']
        )
        self.__create_statistics(created_item, item['statistics'])
        return created_item

    def __create_statistics(self, item, main_statistics):
        rarity = item.rarity
        for statistic in Statistic.STATISTICS:
            name = statistic[0]
            if statistic[0] in main_statistics:
                self.__create_main_statistic(name, rarity, item)
            else:
                self.__create_statistic(name, item)

    def __create_main_statistic(self, name, rarity, item):
        bottom_scope = self.__get_main_statistic_points_bottom_scope(rarity)
        top_scope = self.__get_main_statistic_points_top_scope(rarity)
        random_multiplier = round(random.uniform(bottom_scope, top_scope), 2)
        points = Statistic.POINTS_PER_LEVEL * item.level * random_multiplier
        ItemStatistic.objects.create(
            name=name,
            points=points,
            item=item
        )

    def __create_statistic(self, name, item):
        top_scope = self.__get_statistic_points_top_scope()
        random_multiplier = round(random.uniform(0, top_scope), 2)
        points = Statistic.POINTS_PER_LEVEL * item.level * random_multiplier
        ItemStatistic.objects.create(
            name=name,
            points=points,
            item=item
        )

    def __get_main_statistic_points_top_scope(self, rarity):
        statistic_scope = self.__get_statistic_points_top_scope()
        multiplier = self.RARITY_MULTIPLIERS[rarity['name']]
        return statistic_scope * multiplier
    
    def __get_main_statistic_points_bottom_scope(self, rarity):
        top_scope = self.__get_main_statistic_points_top_scope(rarity)
        bottom_scope = top_scope - self.__get_statistic_points_top_scope()
        return bottom_scope

    def __get_statistic_points_top_scope(self):
        statistics_number = len(Statistic.STATISTICS)
        return 1 / statistics_number
