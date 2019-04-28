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
            },
            {
                'name': 'helmet',
                'description': 'Helmet description',
                'rarity': RARITIES['common'],
                'statistics': [
                    Statistic.HEALTH
                ]
            },
            {
                'name': 'bow',
                'description': 'Bow description',
                'rarity': RARITIES['common'],
                'statistics': [
                    Statistic.AGILITY
                ]
            },
            {
                'name': 'staff',
                'description': 'Staff description',
                'rarity': RARITIES['common'],
                'statistics': [
                    Statistic.INTELLIGENCE
                ]
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
                ]
            },
        ],
    }
}