import os
from random import choice, sample

import requests

path = os.path.dirname(__file__)


def choose_one(filename):
    with open(f'{path}/data/{filename}', 'r') as file:
        l = file.readlines()
    recipe = choice(l)
    return recipe
