# -*- coding: utf-8 -*-
import os
import pygame
import random
import unittest
from enum21 import Enum


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
