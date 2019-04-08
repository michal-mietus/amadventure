from artifical.models import mob


mobs = [
  # TODO maybe I should create python class to operate on this data
  # and subclass some of them, for example
  # bear => mountain_bear
  # bear => forest_bear
  # in that case they would still have the same parent and some of
  # similiar attributes but we will override other, that would
  # limit some lines of this file and work.
  #
  # TODO Don't know how connect classes and locations to operate
  # on variables not on a strings
  {
    'name': 'wolf',
    'description': 'wolf_description',
    'mob_class': 'agile',
    'location': 'forest', # can we add some automatics to this part?
    'difficulty': mob.Mob.MEDIUM,
  },
  {
    'name': 'bear',
    'description': 'bear_description',
    'mob_class': 'physic',
    'location': 'forest',
    'difficulty': mob.Mob.HARD,
  },
  {
    'name': 'snake',
    'description': 'snake_description',
    'mob_class': 'agile',
    'location': 'desert',
    'difficulty': mob.Mob.EASY,
  },
]