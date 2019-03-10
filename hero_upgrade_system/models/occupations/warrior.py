abilities = {}

# attack

def charge():
    pass

abilities['charge'] = {
    'name': 'charge',
    'parent': None,
    'unblock_level': 0,
    'category': 'active',
    'function': 'charge',
}

def super_charge():
    pass

abilities['super_charge'] = {
    'name': 'super_charge',
    'parent': 'charge',
    'unblock_level': 0,
    'category': 'active',
    'function': 'super_charge',
}

# defense

def defender():
    pass

abilities['defender'] = {
    'name': 'defender',
    'parent': None,
    'unblock_level': 0,
    'category': 'passive',
    'function': 'defender',
}

def regeneration():
    pass

abilities['regeneration'] = {
    'name': 'regeneration',
    'parent': 'defender',
    'unblock_level': 0,
    'category': 'passive',
    'function': 'regeneration',
}
