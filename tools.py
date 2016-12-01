# -*- coding: utf-8 -*-
import os
import pygame


def debug(*args):
    for foo in args:
        if hasattr(foo, "__str__"):
            print str(foo),
        else:
            print foo.__class__.__name__,
    print


def load_png(name):  # --> Surface, Rect
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Nie mozna wczytac:', fullname
        raise SystemExit, message
    return image, image.get_rect()


def filtruj_duplikaty(arg):
    se = set(arg)
    return list(se)


def srednia(pos1, pos2):
    return (pos1[0]+pos2[0])/2, pos1[1]+pos2[1]/2


def minus(pos1, pos2):
    return pos1[0]-pos2[0], pos1[1]-pos2[1]
