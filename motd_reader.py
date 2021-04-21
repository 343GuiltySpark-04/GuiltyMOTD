import random

import yaml
from termcolor import cprint

motd_db_path = '/usr/local/games/guiltyMOTD/db/motd_db.yaml'


def motd_generator():
    stream = open(motd_db_path)

    motd_list = yaml.load(stream, Loader=yaml.Loader)

    stream.close()

    index = random.randrange(len(motd_list))

    return motd_list[index]


def color_generator():
    color_list = ['red', 'green', 'yellow', 'blue', 'cyan', 'magenta']

    index = random.randrange(len(color_list))

    return color_list[index]


def read_motd():
    color = color_generator()

    motd = motd_generator()

    cprint(motd, color)
