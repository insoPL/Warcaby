# -*- coding: utf-8 -*-
import pygame
from Pionek import Pionek
from tools import *


class PionkiNaSzachownicy(pygame.sprite.RenderPlain):
    def __init__(self, size_of_one_tile):
        super(pygame.sprite.RenderPlain, self).__init__()

        self._pionki = list()  # lista zawierajaca wszystkie pionki

        def dodaj_pionek(x, y, kolor):  # funkcja pomocnicza
            self.dodaj_pionek(size_of_one_tile, (x, y), kolor)

        for foo in range(0, 8, 2):  # dodaj pionki
            dodaj_pionek(foo+1, 7, Kolor.czarny)  # czarne - dol ekranu
            dodaj_pionek(foo, 6, Kolor.czarny)
            dodaj_pionek(foo+1, 5, Kolor.czarny)

            dodaj_pionek(foo, 2, Kolor.bialy)
            dodaj_pionek(foo+1, 1, Kolor.bialy)  # biale
            dodaj_pionek(foo, 0, Kolor.bialy)

    def dodaj_pionek(self, size_of_one_tile, cords, kolor):
        pionek = Pionek(size_of_one_tile, cords, kolor)
        self._pionki.append(pionek)
        self.add_internal(pionek)

    def usun_pionek(self, cords):
        pionek = self.get_pionek(cords)
        self.remove_internal(pionek)
        self._pionki.remove(pionek)

    def get_pionek(self, cords):  # --> Pionek
        for foo in self._pionki:
            if foo.cords == cords:
                return foo
        debug("nie ma tam pionka!")
        return False

    @property
    def dwie_listy(self):
        biale = list()
        czarne = list()
        for foo in self._pionki:
            if foo.color == Kolor.czarny:
                czarne.append(foo.cords)
            if foo.color == Kolor.bialy:
                biale.append(foo.cords)
        return biale, czarne

