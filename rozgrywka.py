# -*- coding: utf-8 -*-
from tools import *
from pionek import *
from oznaczenie import *
from ruchy import *
import pygame


class Rozgrywka:
    """klasa reprezentujaca szachownice i calą jej zawartość"""
    def __init__(self, screen):
        self.screen = screen
        self.image, self.rect = load_png("szachownica.png")
        self.screen.blit(self.image, self.rect)
        self.kolejnosc = 1  # zaczynają białe

        self.pionki = list()  # lista zawierajaca wszystkie pionki

        for foo in range(0, 8, 2):  # dodaj pionki
            self.pionki.append(Pionek(self.size_of_one_tile, (foo+1, 7), 0))  # czarne - dol ekranu
            self.pionki.append(Pionek(self.size_of_one_tile, (foo, 6), 0))

            self.pionki.append(Pionek(self.size_of_one_tile, (foo+1, 1), 1))  # biale
            self.pionki.append(Pionek(self.size_of_one_tile, (foo, 0), 1))

        self.oznaczone = list()
        self.renderuj_oznaczenie = pygame.sprite.RenderPlain(self.oznaczone)

        self.renderuj_pionki = pygame.sprite.RenderPlain(self.pionki)  # Uchwyt slużący do renderowania pionków

        self.oznacz((0, 0), (1, 1))
        self.odznacz()

        self.przenoszenie = -1

    @property
    def size_of_one_tile(self):
        return self.rect.width/8, self.rect.height/8

    def update(self):
        self.renderuj_pionki.update()
        self.renderuj_pionki.draw(self.screen)

    def oznacz(self, *cords):  # cords - lista krotek (x, y)
        for cord in cords:
            self.oznaczone.append(Oznaczenie(self.size_of_one_tile, cord))
        self.renderuj_oznaczenie.add(self.oznaczone)
        self.renderuj_oznaczenie.update()
        self.renderuj_oznaczenie.draw(self.screen)

    def odznacz(self):
        self.renderuj_oznaczenie.clear(self.screen, self.image)
        self.oznaczone = list()
        self.renderuj_oznaczenie.empty()
        self.renderuj_oznaczenie.update()  # nie potrzebne?
        self.renderuj_oznaczenie.draw(self.screen)

    def get_pionek(self, x, y):
        for foo in self.pionki:
            if foo.cords == (x, y):
                return foo
        debug("nie ma tam pionka!")
        return False

    def pos_to_cords(self, pos):  # change Surface coords to chess cords
        return pos[0] / (self.rect.width / 8), 7 - (pos[1] / (self.rect.height / 8))

    def click(self, pos):
        debug("[klik]: ", pos)
        if self.przenoszenie != -1:  # JEST w trybie przenoszenia
            debug("[klik]: odlozenie!")
            self.screen.blit(self.image, self.przenoszenie.rect, self.przenoszenie.rect)
            if self.czy_jest_oznaczony(*self.pos_to_cords(pos)):
                foo = self.znajdz_bitego(self.przenoszenie.cords, self.pos_to_cords(pos))
                if foo != 0:
                    self.zbij(*foo)
                self.przenoszenie.move(*self.pos_to_cords(pos))
                self.kolejnosc = not self.kolejnosc
            self.przenoszenie = -1
            self.odznacz()
            self.update()

        else:  # NIE jest w trybie przenoszenia
            for pionek in self.pionki:
                if pionek.rect.collidepoint(pos) and self.kolejnosc == pionek.color:
                    debug("[klik]: przenoszenie!")
                    self.przenoszenie = pionek  # przejdz w tryb przenoszenia
                    debug(mozliwe_ruchy2(pionek.cords,pionek.color,*self.dwie_listy))
                    self.oznacz(*mozliwe_ruchy(pionek.cords, pionek.color, self.slownik_uproszczonych_pionkow))

    def czy_jest_oznaczony(self, x, y):
        for ozn in self.oznaczone:
            if ozn.cords == (x, y):
                return True
        return False

    def znajdz_bitego(self, pos1, pos2):
        if pos1[1]-pos2[1] == -2: # jesli biale
            if pos1[0]-pos2[0] == 2:
                return pos1[0]-1, pos1[1]+1
            elif pos1[0]-pos2[0] == -2:
                return pos1[0]+1, pos1[1]+1
        if pos1[1]-pos2[1] == 2: # jesli czarne
            if pos1[0]-pos2[0] == 2:
                return pos1[0]-1, pos1[1]-1
            elif pos1[0]-pos2[0] == -2:
                return pos1[0]+1, pos1[1]-1
        return 0

    @property
    def slownik_uproszczonych_pionkow(self):
        bar = dict()
        for foo in self.pionki:
            bar[foo.cords] = foo.color
        return bar

    @property
    def dwie_listy(self):
        biale = list()
        czarne = list()
        for foo in self.pionki:
            if foo.color == 0:
                czarne.append(foo.cords)
            if foo.color == 1:
                biale.append(foo.cords)
        return biale, czarne

    def zbij(self, x, y):
        for pionek in self.pionki:
            if pionek.cords == (x, y):
                self.renderuj_pionki.remove(pionek)
                self.screen.blit(self.image, pionek.rect, pionek.rect)
                self.pionki.remove(pionek)


