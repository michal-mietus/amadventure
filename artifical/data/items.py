from general_upgrade.models import Statistic
from artifical.model.item import Item


items = [
    {
        'name': 'sword',
        'description': 'Sword description',
        'rarity': Item.COMMON,
        'statistics': [
            Statistic.STRENGTH
        ]
    },
    {
        'name': 'helmet',
        'description': 'Helmet description',
        'rarity': Item.COMMON,
        'statistics': [
            Statistic.HEALTH
        ]
    },
    {
        'name': 'bow',
        'description': 'Bow description',
        'rarity': Item.COMMON,
        'statistics': [
            Statistic.AGILITY
        ]
    },
    {
        'name': 'Staff',
        'description': 'Staff description',
        'rarity': Item.COMMON,
        'statistics': [
            Statistic.INTELLIGENCE
        ]
    },
]