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

def quick_charge():
    pass

abilities['quick_charge'] = {
    'name': 'quick_charge',
    'parent': 'charge',
    'unblock_level': 0,
    'category': 'active',
    'function': 'quick_charge',
}

def ram():
    pass

abilities['ram'] = {
    'name': 'ram',
    'parent': 'super_charge',
    'unblock_level': 0,
    'category': 'active',
    'function': 'ram',
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

def block():
    pass

abilities['block'] = {
    'name': 'block',
    'parent': 'defender',
    'unblock_level': 3,
    'category': 'active',
    'function': 'block',
}

def regeneration():
    pass

abilities['regeneration'] = {
    'name': 'regeneration',
    'parent': None,
    'unblock_level': 0,
    'category': 'passive',
    'function': 'regeneration',
}

def cure():
    pass

abilities['cure'] = {
    'name': 'cure',
    'parent': 'regeneration',
    'unblock_level': 2,
    'category': 'active',
    'function': 'cure',
}
