# -*- coding: utf-8 -*-
from tools import *
from Oznaczenie import Oznaczenie
from PionkiNaSzachownicy import PionkiNaSzachownicy


class Szachownica:
    def __init__(self, screen):
        self.screen = screen
        self.image, self.rect = load_png("szachownica.png")
        self.screen.blit(self.image, self.rect)

        self.pionki = list()  # lista zawierajaca wszystkie pionki

        self.pionkiNaSzachownicy = PionkiNaSzachownicy(self.size_of_one_tile)

        self._oznaczone = list()

        self._renderuj_oznaczenie = pygame.sprite.RenderPlain(self._oznaczone)

    def przesun_pionek(self, przesowany_pionek, cordy_docelowe):
        self.czysc_fragment_ekranu(przesowany_pionek.rect)  # wyczyszczenie ekranu pod starym pionkiem
        przesowany_pionek.move(*cordy_docelowe)  # przeniesienie pionka na nowe pole

    def dodaj_pionek(self, cords, kolor):
        self.pionkiNaSzachownicy.dodaj_pionek(self.size_of_one_tile, cords, kolor)

    def get_pionek(self, cords):
        return self.pionkiNaSzachownicy.get_pionek(cords)

    @property
    def size_of_one_tile(self):
        return self.rect.width/8, self.rect.height/8

    @property
    def dwie_listy(self):
        return self.pionkiNaSzachownicy.dwie_listy

    def update(self):
        self.pionkiNaSzachownicy.update()
        self.pionkiNaSzachownicy.draw(self.screen)

    def czysc_fragment_ekranu(self, rect):
        self.screen.blit(self.image, rect, rect)

    def pos_to_cords(self, pos):  # change Surface coords to chess cords
        return pos[0] / (self.rect.width / 8), 7 - (pos[1] / (self.rect.height / 8))

    def zbij_pionek(self, cords):
        pionek = self.pionkiNaSzachownicy.get_pionek(cords)
        self.pionkiNaSzachownicy.usun_pionek(cords)
        self.czysc_fragment_ekranu(pionek.rect)

    def oznacz_pole(self, *cords):  # cords - lista krotek (x, y)
        for cord in cords:
            self._oznaczone.append(Oznaczenie(self.size_of_one_tile, cord))
        self._renderuj_oznaczenie.add(self._oznaczone)
        self._renderuj_oznaczenie.update()
        self._renderuj_oznaczenie.draw(self.screen)

    def odznacz_wszystkie_pola(self):
        self._renderuj_oznaczenie.clear(self.screen, self.image)
        self._oznaczone = list()
        self._renderuj_oznaczenie.empty()
        self._renderuj_oznaczenie.update()  # nie potrzebne?
        self._renderuj_oznaczenie.draw(self.screen)
