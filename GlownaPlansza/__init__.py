# -*- coding: utf-8 -*-

from Pionek import Pionek
from Oznaczenie import Oznaczenie
from AI import ai
from ruchy import *
from Szachownica import Szachownica
from tools import *


class GlownaPlansza(Szachownica):
    """klasa reprezentujaca szachownice i calą jej zawartość"""
    def __init__(self, screen):
        Szachownica.__init__(self, screen)
        self.czyja_kolej = Kolor.bialy  # zaczynają białe
        self._ruchy = dict()  # przechowuje dane o mozliwych ruchach
        self.tryb_jednego_gracza = True
        self.przesowany_pionek = None
        self.tryb_przenoszenia = False

        self.w_trakcie_ruchy = False
        self.wszystkie_mozliwe_ruchy = dict()
        self.poczatek_ruchu_gracza(Kolor.bialy)

    def poczatek_ruchu_gracza(self, kolor_gracza):
        if kolor_gracza == Kolor.bialy:
            debug("Początek ruchu bialego gracza")
            pionki_gracza, pionki_przeciwnika = self.dwie_listy
        elif kolor_gracza == Kolor.czarny:
            debug("Początek ruchu czarnego gracza")
            pionki_przeciwnika, pionki_gracza = self.dwie_listy
        else:
            raise ValueError

        self.wszystkie_mozliwe_ruchy = dict()
        for cordy_pionka in pionki_gracza:
            mozliwe_bicia_pionka = mozliwe_bicia(cordy_pionka, kolor_gracza, *self.dwie_listy)
            if len(mozliwe_bicia_pionka) != 0:
                self.wszystkie_mozliwe_ruchy[cordy_pionka] = mozliwe_bicia_pionka
        if len(self.wszystkie_mozliwe_ruchy) == 0:
            for cordy_pionka in pionki_gracza:
                mozliwe_ruchy_pionka = mozliwe_ruchy(cordy_pionka, kolor_gracza, *self.dwie_listy)
                if len(mozliwe_ruchy_pionka) != 0:
                    self.wszystkie_mozliwe_ruchy[cordy_pionka] = mozliwe_ruchy_pionka
        if len(self.wszystkie_mozliwe_ruchy) == 0:
            raise BrakMozliwegoRuchu

    def on_click(self, pos):
        cordy_kliknietego_pola = self.pos_to_cords(pos)

        if not self.tryb_przenoszenia:  # NIE jest w trybie podniesionego pionka
            pionek = self.get_pionek(cordy_kliknietego_pola)
            if pionek is not None and pionek.color == self.czyja_kolej and cordy_kliknietego_pola in self.wszystkie_mozliwe_ruchy.keys():
                debug("[on_click]: Podniesienie Pionka!")
                self._ruchy = mozliwe_bicia(pionek.cords, pionek.color, *self.dwie_listy)
                if len(self._ruchy) == 0:
                    self._ruchy = mozliwe_ruchy(pionek.cords, pionek.color, *self.dwie_listy)
                self.oznacz_pole(*self._ruchy.keys())
                self.podnies_pionek(pionek)

        else:  # JEST w trybie podniesionego pionka
            debug("[on_click]: Opuszczenie Pionka!")
            if cordy_kliknietego_pola in self._ruchy:
                self.przesun_pionek(self.przesowany_pionek, cordy_kliknietego_pola)
                self.pionkiNaSzachownicy.dodaj_pionek(self.przesowany_pionek)
                self.czyja_kolej = not self.czyja_kolej  # koniec ruchu
                self.wszystkie_mozliwe_ruchy = dict()
                if self._ruchy[cordy_kliknietego_pola] != 0:
                    self.usun_pionek(self._ruchy[cordy_kliknietego_pola])
                    moze_jeszcze_bic = mozliwe_bicia(self.przesowany_pionek.cords, self.przesowany_pionek.color, *self.dwie_listy)
                    if len(moze_jeszcze_bic) != 0:
                        self.wszystkie_mozliwe_ruchy[self.przesowany_pionek.cords] = moze_jeszcze_bic
                        self.czyja_kolej = not self.czyja_kolej

                if self.tryb_jednego_gracza and len(self.wszystkie_mozliwe_ruchy) == 0:
                    self.ruch_ai()
                    self.poczatek_ruchu_gracza(self.czyja_kolej)
                elif len(self.wszystkie_mozliwe_ruchy) == 0:
                    self.poczatek_ruchu_gracza(self.czyja_kolej)

            else:
                self.pionkiNaSzachownicy.dodaj_pionek(self.przesowany_pionek)

            self._ruchy = dict()
            self.odznacz_wszystkie_pola()
            self.update()
            self.opuszczenie_pionka()

    def opuszczenie_pionka(self):
        self.tryb_przenoszenia = False
        raise OpuszczeniePionka

    def podnies_pionek(self, pionek):
        self.usun_pionek(pionek.cords)
        self.przesowany_pionek = pionek  # przejdz w tryb przenoszenia
        self.tryb_przenoszenia = True
        raise PodniesieniePionka(pionek.color)

    def ruch_ai(self):
        debug("[AI]: Rozpoczecie pracy AI")
        try:
            cordy_pionka, cordy_docelowe, zbite_pole = ai(*self.dwie_listy)
        except BrakMozliwegoRuchu:
            raise BrakMozliwegoRuchu
        debug("[AI]: Zakonczylo prace wybierając ruch", cordy_pionka, "->", cordy_docelowe)

        if zbite_pole != 0:
            self.usun_pionek(zbite_pole)
        self.przesun_pionek(self.get_pionek(cordy_pionka), cordy_docelowe)
        self.czyja_kolej = not self.czyja_kolej
