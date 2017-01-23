# -*- coding: utf-8 -*-
from Pionek import Pionek
from tools import *
from Oznaczenie import Oznaczenie


class Szachownica:
    def __init__(self, screen):
        self.screen = screen
        self.image, self.rect = load_png("szachownica.png")
        self.screen.blit(self.image, self.rect)

        self.pionki = list()  # lista zawierajaca wszystkie pionki

        for foo in range(0, 8, 2):  # dodaj pionki
            self.dodaj_pionek(foo+1, 7, Kolor.czarny)  # czarne - dol ekranu
            self.dodaj_pionek(foo, 6, Kolor.czarny)
            self.dodaj_pionek(foo+1, 5, Kolor.czarny)

            self.dodaj_pionek(foo, 2, Kolor.bialy)
            self.dodaj_pionek(foo+1, 1, Kolor.bialy)  # biale
            self.dodaj_pionek(foo, 0, Kolor.bialy)

        self.renderuj_pionki = pygame.sprite.RenderPlain(self.pionki)  # Uchwyt slużący do renderowania pionków

        self._oznaczone = list()

        self._renderuj_oznaczenie = pygame.sprite.RenderPlain(self._oznaczone)

    def dodaj_pionek(self, x, y, kolor):
        self.pionki.append(Pionek(self.size_of_one_tile, (x, y), kolor))

    def przesun_pionek(self, przesowany_pionek, cordy_docelowe):
        self.czysc_fragment_ekranu(przesowany_pionek.rect)  # wyczyszczenie ekranu pod starym pionkiem
        przesowany_pionek.move(*cordy_docelowe)  # przeniesienie pionka na nowe pole

    @property
    def size_of_one_tile(self):
        return self.rect.width/8, self.rect.height/8

    def update(self):
        self.renderuj_pionki.update()
        self.renderuj_pionki.draw(self.screen)

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

    @property
    def dwie_listy(self):
        biale = list()
        czarne = list()
        for foo in self.pionki:
            if foo.color == Kolor.czarny:
                czarne.append(foo.cords)
            if foo.color == Kolor.bialy:
                biale.append(foo.cords)
        return biale, czarne

    def zbij_pionek(self, x, y):
        pionek = self.get_pionek(x, y)
        self.renderuj_pionki.remove(pionek)
        self.czysc_fragment_ekranu(pionek.rect)
        self.pionki.remove(pionek)

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
