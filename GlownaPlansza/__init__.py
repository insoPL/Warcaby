# -*- coding: utf-8 -*-

from Pionek import Pionek
from Oznaczenie import Oznaczenie
from AI import ai
from ruchy import mozliwe_ruchy
from Szachownica import Szachownica
from tools import *


class GlownaPlansza(Szachownica):
    """klasa reprezentujaca szachownice i calą jej zawartość"""
    def __init__(self, screen):
        Szachownica.__init__(self, screen)
        self.czyja_kolej = Kolor.bialy  # zaczynają białe
        self._ruchy = dict()  # przechowuje dane o mozliwych ruchach
        self.tryb_jenego_gracza = True
        self.przesowany_pionek = None
        self.tryb_przenoszenia = False

    def on_click(self, pos):
        debug("[on_click]: ", pos)

        if not self.tryb_przenoszenia:  # NIE jest w trybie podniesionego pionka
            pionek = self.get_pionek(*self.pos_to_cords(pos))
            if pionek != 0 and pionek.color == self.czyja_kolej:
                debug("[on_click]: przenoszenie!")
                self.przesowany_pionek = pionek  # przejdz w tryb przenoszenia
                self.tryb_przenoszenia = True
                self._ruchy = mozliwe_ruchy(pionek.cords, pionek.color, *self.dwie_listy)
                self.oznacz_pole(*self._ruchy.keys())

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

            self.tryb_przenoszenia = False
            self._ruchy = dict()
            self.odznacz_wszystkie_pola()
            self.update()

    def ruch_ai(self):
        try:
            cordy_pionka, cordy_docelowe, zbite_pole = ai(*self.dwie_listy)
        except BrakMozliwegoRuchu:
            raise BrakMozliwegoRuchu
        if zbite_pole != 0:
            self.zbij_pionek(*zbite_pole)
        przenoszony_pionek = self.get_pionek(*cordy_pionka)
        self.czysc_fragment_ekranu(przenoszony_pionek.rect)
        przenoszony_pionek.move(*cordy_docelowe)
        self.czyja_kolej = not self.czyja_kolej
