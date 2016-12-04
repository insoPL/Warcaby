# -*- coding: utf-8 -*-
import os
import pygame
import random

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


def max_value_dict(dic):
    maxim = 0
    for value in dic.values():
        if maxim < value:
            maxim = value
    ret_dic = dict()
    for x,y in dic.keys():
        if y == maxim:
            ret_dic[x] = y
    return ret_dic


def random_max_value(dic):
    maxim = 0
    for value in dic.values():
        if maxim < value:
            maxim = value
    ret_dic = dict()
    for x, y in dic.items():
        if y == maxim:
            ret_dic[x] = y
    if len(ret_dic) !=0:
        return random.choice(ret_dic.keys())


def random_max_value2(dic):
    maxim = 0
    for value in dic:
        if maxim < value[2]:
            maxim = value[2]
    ret_dic = list()
    for x, y, z in dic:
        if z == maxim:
            ret_dic = (x, y, z)
    if len(ret_dic) != 0:
        return random.choice(ret_dic)


# ####################################nie uzywane


def srednia(pos1, pos2):
    return (pos1[0]+pos2[0])/2, pos1[1]+pos2[1]/2


def minus(pos1, pos2):
    return pos1[0]-pos2[0], pos1[1]-pos2[1]
