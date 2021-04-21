from os import name

from termcolor import cprint

from motd_reader import read_motd


def check_is_posix():
    if name != 'posix':
        exit(cprint("DO PEOPLE EVEN RTFM ANYMORE? YOU NEED TO RUN THIS PROGRAM ON A POSIX SYSTEM!", 'red',
                    attrs=['bold', 'underline']))
    else:
        read_motd()


check_is_posix()
