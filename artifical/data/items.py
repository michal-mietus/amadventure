from general_upgrade.models import Statistic
from artifical.models.item import ItemGeneral

# what about graphics?
# should items be grouped by rarity?

RARITIES = {
    'common': {
    'name': 'common',
    'chance': 1  
    },
    'rare': {
    'name': 'rare',
    'chance': 0.3  
    },
    'epic': {
    'name': 'epic',
    'chance': 0.1  
    },
    'legendary': {
    'name': 'legendary',
    'chance': 0.03
    },
}

items = {
    'rarity': {
        'common': {
            'sword': {
                'rarity': ItemGeneral.RARITIES['common'],
                'description': 'Sword description',
                'statistics': [
                    Statistic.STRENGTH
                ],
            },
            'helmet': {
                'description': 'Helmet description',
                'rarity': ItemGeneral.RARITIES['common'],
                'statistics': [
                    Statistic.HEALTH
                ]
            },
            'bow': {
                'description': 'Bow description',
                'rarity': ItemGeneral.RARITIES['common'],
                'statistics': [
                    Statistic.AGILITY
                ]
            },
            'staff': {
                'description': 'Staff description',
                'rarity': ItemGeneral.RARITIES['common'],
                'statistics': [
                    Statistic.INTELLIGENCE
                ]
            },
        },
        
        'rare':
        {
            'necklace': {
                'description': 'Necklace description',
                'rarity': ItemGeneral.RARITIES['rare'],
                'statistics': [
                    Statistic.INTELLIGENCE,
                    Statistic.HEALTH,
                ]
            },
        },
    }
}