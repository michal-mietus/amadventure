from general_upgrade.models import Statistic
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
        'common': [
            {
                'name': 'sword',
                'rarity': RARITIES['common'],
                'description': 'Sword description',
                'statistics': [
                    Statistic.STRENGTH
                ],
                'image': 'swords/sword_1.jpg',
            },
            {
                'name': 'helmet',
                'description': 'Helmet description',
                'rarity': RARITIES['common'],
                'statistics': [
                    Statistic.HEALTH
                ],
                'image': 'helmets/helmet_1.jpg',
            },
            {
                'name': 'bow',
                'description': 'Bow description',
                'rarity': RARITIES['common'],
                'statistics': [
                    Statistic.AGILITY
                ],
                'image': 'bows/bow_1.jpg',
            },
            {
                'name': 'Wand',
                'description': 'Wand description',
                'rarity': RARITIES['common'],
                'statistics': [
                    Statistic.INTELLIGENCE
                ],
                'image': 'wands/magic_wand_1.jpg',
            },
        ],
        
        'rare':
        [
            {
                'name': 'necklace',
                'description': 'Necklace description',
                'rarity': RARITIES['rare'],
                'statistics': [
                    Statistic.INTELLIGENCE,
                    Statistic.HEALTH,
                ],
                'image': 'spelbooks/spelbook_9.jpg',
            },
        ],
    }
}