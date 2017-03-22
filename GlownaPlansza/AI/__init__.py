# -*- coding: utf-8 -*-

from tools import *
from ai_tools import *
import unittest


def ai(lista_bialych, lista_czarnych):
    mozliwe_ruchy_wszystkich_pionkow = znajdz_wszelkie_mozliwe_ruchy(lista_bialych, lista_czarnych, 0)
    wyniki = list()
    for cordy_pionka, cordy_docelowe, cordy_zbitego in mozliwe_ruchy_wszystkich_pionkow:
        nowa_lista_czarnych = przesun_pionek_na_liscie(lista_czarnych, cordy_pionka, cordy_docelowe)
        if cordy_zbitego != 0:
            nowa_lista_bialych = usun_pionek_z_listy(lista_bialych, cordy_zbitego)
        else:
            nowa_lista_bialych = lista_bialych
        deep = 4
        wynik = _ai_rek(nowa_lista_bialych, nowa_lista_czarnych, 1, deep)

        wyniki.append((cordy_pionka, cordy_docelowe, wynik, cordy_zbitego))
        debug("[AI] wartosc ruchu", cordy_pionka, "->", cordy_docelowe, ": ", wynik)
    return random_max_ruch(wyniki)


def _ai_rek(lista_bialych, lista_czarnych, kolor_robiacy_ruch, deep):
    min_max_value = None
    if deep == 0:
        return len(lista_czarnych) - len(lista_bialych)
    deep -= 1  # ogranicznik głębokości

    mozliwe_ruchy_wszystkich_pionkow = znajdz_wszelkie_mozliwe_ruchy(lista_bialych, lista_czarnych, kolor_robiacy_ruch)

    if len(mozliwe_ruchy_wszystkich_pionkow) == 0:
        return len(lista_czarnych) - len(lista_bialych)

    if kolor_robiacy_ruch == Kolor.czarny:
        for cordy_pionka, cordy_docelowe, cordy_zbitego in mozliwe_ruchy_wszystkich_pionkow:
            nowa_lista_czarnych = przesun_pionek_na_liscie(lista_czarnych, cordy_pionka, cordy_docelowe)
            if cordy_zbitego != 0:
                nowa_lista_bialych = usun_pionek_z_listy(lista_bialych, cordy_zbitego)
            else:
                nowa_lista_bialych = lista_bialych
            wynik_rekurencji = _ai_rek(nowa_lista_bialych, nowa_lista_czarnych, not kolor_robiacy_ruch, deep)
            min_max_value = max_wynik(min_max_value, wynik_rekurencji)
    elif kolor_robiacy_ruch == Kolor.bialy:
        for cordy_pionka, cordy_docelowe, cordy_zbitego in mozliwe_ruchy_wszystkich_pionkow:
            nowa_lista_bialych = przesun_pionek_na_liscie(lista_bialych, cordy_pionka, cordy_docelowe)
            if cordy_zbitego != 0:
                nowa_lista_czarnych = usun_pionek_z_listy(lista_czarnych, cordy_zbitego)
            else:
                nowa_lista_czarnych = lista_czarnych
            wynik_rekurencji = _ai_rek(nowa_lista_bialych, nowa_lista_czarnych, Kolor.czarny, deep)
            min_max_value = min_wynik(min_max_value, wynik_rekurencji)
    return min_max_value


class TestAI(unittest.TestCase):
    def testBrakMozliwychRuchow(self):
        self.assertRaises(BrakMozliwegoRuchu, ai, [], [])
        self.assertRaises(BrakMozliwegoRuchu, ai, [], [(2,0)])
        self.assertRaises(BrakMozliwegoRuchu, ai, [(0,0),(2,0)], [(1,1)])

    def testProstychRuchow(self):
        self.assertEqual(ai([], [(7,7)]), ((7,7), (6,6), 0))
        self.assertEqual(ai([(0,6)], [(1,7)]), ((1,7), (2,6), 0))

    def testProstyRuchBijacy(self):
        self.assertEqual(ai([(1,1)],[(2,2)]),((2,2),(0,0),(1,1)))
        self.assertEqual(ai([(7,3),(5,3)],[(6,4)]),((6,4),(4,2),(5,3)))

    def testUnikanieRuchowZbijajacych(self):
        self.assertEqual(ai([(1,1)],[(3,3)]),((3,3),(4,2),0))
        self.assertEqual(ai([(2,2),(1,1)],[(3,3),(7,7)]),((3,3),(4,2),0))

    def testPrzewidywaniaRuchowPrzeciwnika(self):
        self.assertEqual(ai([(0,0),(2,2),(4,2)],[(3,3)]),((3,3),(5,1),(4,2)))
