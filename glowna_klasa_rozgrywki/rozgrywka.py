# -*- coding: utf-8 -*-

from pionek import Pionek
from oznaczenie import Oznaczenie
from AI import ai
from ruchy import mozliwe_ruchy
from tools import *
import random
import pygame


class Rozgrywka:
    """klasa reprezentujaca szachownice i calą jej zawartość"""
    def __init__(self, screen):
        random.seed()
        self.screen = screen
        self.image, self.rect = load_png("szachownica.png")
        self.screen.blit(self.image, self.rect)
        self.czyja_kolej = Color.white  # zaczynają białe
        self._ruchy = dict()  # przechowuje dane o mozliwych ruchach
        self.tryb_jenego_gracza = True

        self.pionki = list()  # lista zawierajaca wszystkie pionki

        for foo in range(0, 8, 2):  # dodaj pionki
            self.pionki.append(Pionek(self.size_of_one_tile, (foo+1, 7), Color.black))  # czarne - dol ekranu
            self.pionki.append(Pionek(self.size_of_one_tile, (foo, 6), Color.black))
            self.pionki.append(Pionek(self.size_of_one_tile, (foo+1, 5), Color.black))

            self.pionki.append(Pionek(self.size_of_one_tile, (foo, 2), Color.white))
            self.pionki.append(Pionek(self.size_of_one_tile, (foo+1, 1), Color.white))  # biale
            self.pionki.append(Pionek(self.size_of_one_tile, (foo, 0), Color.white))

        self._oznaczone = list()

        self._renderuj_oznaczenie = pygame.sprite.RenderPlain(self._oznaczone)

        self.renderuj_pionki = pygame.sprite.RenderPlain(self.pionki)  # Uchwyt slużący do renderowania pionków

        self.przesowany_pionek = -1

    @property
    def size_of_one_tile(self):
        return self.rect.width/8, self.rect.height/8

    def update(self):
        self.renderuj_pionki.update()
        self.renderuj_pionki.draw(self.screen)

    def oznacz(self, *cords):  # cords - lista krotek (x, y)
        for cord in cords:
            self._oznaczone.append(Oznaczenie(self.size_of_one_tile, cord))
        self._renderuj_oznaczenie.add(self._oznaczone)
        self._renderuj_oznaczenie.update()
        self._renderuj_oznaczenie.draw(self.screen)

    def odznacz(self):  # odznacz wszystkie pola
        self._renderuj_oznaczenie.clear(self.screen, self.image)
        self._oznaczone = list()
        self._renderuj_oznaczenie.empty()
        self._renderuj_oznaczenie.update()  # nie potrzebne?
        self._renderuj_oznaczenie.draw(self.screen)

    def get_pionek(self, x, y):  # --> Pionek
        for foo in self.pionki:
            if foo.cords == (x, y):
                return foo
        debug("nie ma tam pionka!")
        return False

    def czysc_fragment_ekranu(self, rect):
        self.screen.blit(self.image, rect, rect)

    def pos_to_cords(self, pos):  # change Surface coords to chess cords
        return pos[0] / (self.rect.width / 8), 7 - (pos[1] / (self.rect.height / 8))

    def on_click(self, pos):
        debug("[on_click]: ", pos)

        if self.przesowany_pionek == -1:  # NIE jest w trybie podniesionego pionka
            pionek = self.get_pionek(*self.pos_to_cords(pos))
            if pionek != 0 and self.czyja_kolej == pionek.color:
                debug("[on_click]: przenoszenie!")
                self.przesowany_pionek = pionek  # przejdz w tryb przenoszenia
                self._ruchy = mozliwe_ruchy(pionek.cords, pionek.color, *self.dwie_listy)
                self.oznacz(*self._ruchy.keys())

        else:  # JEST w trybie podniesionego pionka
            debug("[on_click]: odlozenie!")
            if (self.pos_to_cords(pos)) in self._ruchy:
                zbity_pionek = self._ruchy[self.pos_to_cords(pos)]  # zbicie pionka, jeśli jakiś jest do zbicia
                if zbity_pionek != 0:
                    self.zbij_pionek(*zbity_pionek)

                self.czysc_fragment_ekranu(self.przesowany_pionek.rect)  # wyczyszczenie ekranu pod starym pionkiem
                self.przesowany_pionek.move(*self.pos_to_cords(pos))  # przeniesienie pionka na nowe pole

                self.czyja_kolej = not self.czyja_kolej  # koniec ruchu

                if self.tryb_jenego_gracza:
                    self.ruch_ai()

            self.przesowany_pionek = -1
            self._ruchy = dict()
            self.odznacz()
            self.update()

    def ruch_ai(self):
        ruch_ai = ai(*self.dwie_listy)
        if ruch_ai is not None:
            if ruch_ai[2] != 0:
                self.zbij_pionek(*ruch_ai[2])
            przenoszony_pionek = self.get_pionek(*ruch_ai[0])
            self.czysc_fragment_ekranu(przenoszony_pionek.rect)
            przenoszony_pionek.move(*ruch_ai[1])
        self.czyja_kolej = not self.czyja_kolej

    @property
    def dwie_listy(self):
        biale = list()
        czarne = list()
        for foo in self.pionki:
            if foo.color == Color.black:
                czarne.append(foo.cords)
            if foo.color == Color.white:
                biale.append(foo.cords)
        return biale, czarne

    def zbij_pionek(self, x, y):
        pionek = self.get_pionek(x, y)
        self.renderuj_pionki.remove(pionek)
        self.czysc_fragment_ekranu(pionek.rect)
        self.pionki.remove(pionek)