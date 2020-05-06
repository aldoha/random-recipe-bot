import os
from random import choice, sample

import requests

path = os.path.dirname(__file__)


def choose_one(filename):
    with open(f'{path}/{filename}', 'r') as file:
        l = file.readlines()
    recipe = choice(l)
    return recipe


def choose_bunch(filename, count=7):
    with open(f'{path}/{filename}', 'r') as file:
        l = file.readlines()
    recipies = sample(l, count)
    return ''.join(recipies)
