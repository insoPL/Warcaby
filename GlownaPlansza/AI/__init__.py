# -*- coding: utf-8 -*-

from tools import *
from ai_tools import *
import unittest
from GlownaPlansza.ruchy import mozliwe_bicia


def ai(lista_bialych, lista_czarnych):
    lista_podwojnie_zbitych = list()
    wyniki = list()
    mozliwe_ruchy_wszystkich_pionkow = znajdz_wszelkie_mozliwe_ruchy(lista_bialych, lista_czarnych, 0)
    for cordy_pionka, cordy_docelowe, cordy_zbitego in mozliwe_ruchy_wszystkich_pionkow:
        nowa_lista_czarnych = przesun_pionek_na_liscie(lista_czarnych, cordy_pionka, cordy_docelowe)
        if cordy_zbitego != 0:
            nowa_lista_bialych = usun_pionek_z_listy(lista_bialych, cordy_zbitego)
            cordy_docelowe, lista_podwojnie_zbitych = _ai_rek_podwojne_bicie(nowa_lista_bialych, nowa_lista_czarnych, Kolor.czarny, cordy_docelowe)
            for foo in lista_podwojnie_zbitych:
                nowa_lista_bialych = usun_pionek_z_listy(nowa_lista_bialych, foo)
            lista_podwojnie_zbitych.append(cordy_zbitego)
        else:
            nowa_lista_bialych = lista_bialych
        deep = 4
        wynik = _ai_rek(nowa_lista_bialych, nowa_lista_czarnych, 1, deep)

        wyniki.append((cordy_pionka, cordy_docelowe, wynik, lista_podwojnie_zbitych))
        debug("[AI] wartosc ruchu", cordy_pionka, "->", cordy_docelowe, ": ", lista_podwojnie_zbitych)
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
                cordy_docelowe, lista_podwojnie_zbitych = _ai_rek_podwojne_bicie(nowa_lista_bialych,nowa_lista_czarnych,kolor_robiacy_ruch,cordy_docelowe)
                for foo in lista_podwojnie_zbitych:
                    nowa_lista_bialych = usun_pionek_z_listy(nowa_lista_bialych, foo)
            else:
                nowa_lista_bialych = lista_bialych
            wynik_rekurencji = _ai_rek(nowa_lista_bialych, nowa_lista_czarnych, not kolor_robiacy_ruch, deep)
            min_max_value = max_wynik(min_max_value, wynik_rekurencji)
    elif kolor_robiacy_ruch == Kolor.bialy:
        for cordy_pionka, cordy_docelowe, cordy_zbitego in mozliwe_ruchy_wszystkich_pionkow:
            nowa_lista_bialych = przesun_pionek_na_liscie(lista_bialych, cordy_pionka, cordy_docelowe)
            if cordy_zbitego != 0:
                nowa_lista_czarnych = usun_pionek_z_listy(lista_czarnych, cordy_zbitego)
                cordy_docelowe, lista_podwojnie_zbitych = _ai_rek_podwojne_bicie(nowa_lista_bialych,nowa_lista_czarnych,kolor_robiacy_ruch,cordy_docelowe)
                for foo in lista_podwojnie_zbitych:
                    nowa_lista_czarnych = usun_pionek_z_listy(nowa_lista_czarnych, foo)
            else:
                nowa_lista_czarnych = lista_czarnych
            wynik_rekurencji = _ai_rek(nowa_lista_bialych, nowa_lista_czarnych, Kolor.czarny, deep)
            min_max_value = min_wynik(min_max_value, wynik_rekurencji)
    return min_max_value


def _ai_rek_podwojne_bicie(lista_bialych, lista_czarnych, kolor_robiacy_ruch, cordy):
    mozliwe_ruchy_bijace = mozliwe_bicia(cordy,kolor_robiacy_ruch,lista_bialych,lista_czarnych)
    mozliwe_wyniki = list()
    for cordy_docelowe, cordy_zbite in mozliwe_ruchy_bijace.items():
        debug(cordy_docelowe, cordy_zbite)
        if kolor_robiacy_ruch == Kolor.czarny:
            nowa_lista_czarnych = przesun_pionek_na_liscie(lista_czarnych, cordy, cordy_docelowe)
            nowa_lista_bialych = usun_pionek_z_listy(lista_bialych,cordy_zbite)
        elif kolor_robiacy_ruch == Kolor.bialy:
            nowa_lista_bialych = przesun_pionek_na_liscie(lista_bialych,cordy, cordy_docelowe)
            nowa_lista_czarnych = usun_pionek_z_listy(lista_czarnych,cordy_zbite)
        else:
            raise ValueError
        cordy_docelowe, zwrocona_lista = _ai_rek_podwojne_bicie(nowa_lista_bialych, nowa_lista_czarnych, kolor_robiacy_ruch, cordy_docelowe)
        ret_list =[cordy_zbite]
        ret_list.extend(zwrocona_lista)
        mozliwe_wyniki.append((cordy_docelowe,ret_list))

    najlepszy_wynik = 0
    najepszy_wynik_zawartosc = (cordy,list())
    for cordy_docelowe_wyniku, ret_list_wyniku in mozliwe_wyniki: # porwonanie wynikow - czesc zwijajaca
        if len(ret_list_wyniku)>najlepszy_wynik:
            najepszy_wynik_zawartosc = (cordy_docelowe_wyniku, ret_list_wyniku)
            najlepszy_wynik = len(ret_list_wyniku)

    return najepszy_wynik_zawartosc


class TestAI(unittest.TestCase):
    def testBrakMozliwychRuchow(self):
        self.assertRaises(BrakMozliwegoRuchu, ai, [], [])
        self.assertRaises(BrakMozliwegoRuchu, ai, [], [(2,0)])
        self.assertRaises(BrakMozliwegoRuchu, ai, [(0,0),(2,0)], [(1,1)])

    def testProstychRuchow(self):
        wynik = ai([], [(7,7)])
        self.assertEqual(wynik, ((7,7), (6,6), []))

        wynik = ai([(0,6)], [(1,7)])
        self.assertEqual(wynik, ((1,7), (2,6), []))

    def testProstyRuchBijacy(self):
        wynik = ai([(1,1)],[(2,2)])
        self.assertEqual(wynik,((2,2),(0,0),[(1,1)]))

        wynik = ai([(7,3),(5,3)],[(6,4)])
        self.assertEqual(wynik,((6,4),(4,2),[(5,3)]))

    def testUnikanieRuchowZbijajacych(self):
        wynik = ai([(1,1)],[(3,3)])
        self.assertEqual(wynik,((3,3),(4,2),[]))

        wynik = ai([(2,2),(1,1)],[(3,3),(7,7)])
        self.assertEqual(wynik,((3,3),(4,2),[]))

    def testPrzewidywaniaRuchowPrzeciwnika(self):
        wynik = ai([(0,0),(2,2),(4,2)],[(3,3)])
        self.assertEqual(wynik,((3,3),(5,1),[(4,2)]))

    def testPodwojnegoBicia(self):
        wynik = ai([(1,1),(3,3),(5,3)],[(4,4)])
        self.assertEqual(wynik,((4,4),(0,0),[(1,1),(3,3)]))

    def testFunkcjiBocznejRekurencyjnejPodwojnegoBicia(self):
        wynik = _ai_rek_podwojne_bicie([(1,1),(3,3)],[(4,4)],Kolor.czarny,(4,4))
        self.assertEqual(wynik, ((0,0),[(3,3),(1,1)]))

        wynik = _ai_rek_podwojne_bicie([(1,1),(3,3),(5,3)],[(4,4)],Kolor.czarny,(4,4))
        self.assertEqual(wynik, ((0,0),[(3,3),(1,1)]))