"""
Holds utilities functions.
"""

import random


FORBIDDEN_IDS = [
    114422335555551,
    737377711111733,
    654365436543654,
    999999999999991,
    111111111111120,
]


FIRST_NAMES = [
    'Marwan',
    'Thomas',
    'Olivier',
    'Gui',
    'Alex',
    'Romain',
    'Antoine',
    'Nicolas',
    'Hiep',
    'Jiwen',
    'Brandon',
    'Brenda',
    'Donald',
]


LAST_NAMES = [
    'Trump',
    'Jones',
    'Smith',
    'Dupont',
    'Durand',
    'Macron',
    'Sarkozy',
    'Hollande',
    'Poutou',
    'Kent',
    'Banner',
    'Wayne',
]


def get_random_first_name():
    """
    Returns a random firstname.
    """
    return random.choice(FIRST_NAMES)


def get_random_last_name():
    """
    Returns a random lastname.
    """
    return random.choice(LAST_NAMES)
