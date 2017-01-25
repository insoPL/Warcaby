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
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Nie mozna wczytac:', fullname
        raise SystemExit(message)
    return image, image.get_rect()


def filtruj_duplikaty(arg):
    se = set(arg)
    return list(se)


class BrakMozliwegoRuchu(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Brak mozliwego ruchu. Koniec gry!"


class PodniesieniePionka(Exception):
    def __init__(self, kolor):
        self.kolor = kolor

    def __str__(self):
        return "Podniesiono " + str(self.kolor)


class OpuszczeniePionka(Exception):
    pass


class Kolor:
    czarny = 0
    bialy = 1

    @staticmethod
    def to_str(kolor):
        if kolor == Kolor.bialy:
            return "bialy"
        elif kolor == Kolor.czarny:
            return "czarny"
        else:
            raise ValueError("Nie wlasciwy Kolor: " + str(kolor))

    @staticmethod
    def przeciwny(kolor):
        if kolor == Kolor.bialy:
            return Kolor.czarny
        elif kolor == Kolor.czarny:
            return Kolor.bialy
        else:
            raise ValueError("Nie wlasciwy Kolor: " + str(kolor))
