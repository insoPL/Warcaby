# -*- coding: utf-8 -*-

import random
from ..ruchy import mozliwe_ruchy
from tools import *
from ai_tools import *


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
        debug("wynik dla", cordy_pionka, "->", cordy_docelowe, ": ", wynik)
    return random_max_ruch(wyniki)


def _ai_rek(lista_przeciwnika, lista_gracza, kolor, deep):  # zwraca (skad, dokad, ile_zbije, co_zbije)
    if deep == 0:
        return len(lista_gracza) - len(lista_przeciwnika)
    deep -= 1  # ogranicznik głębokości

    mozliwe_ruchy_wszystkich_pionkow = znajdz_wszelkie_mozliwe_ruchy(lista_przeciwnika, lista_gracza, kolor)

    if len(mozliwe_ruchy_wszystkich_pionkow) == 0:
        return len(lista_gracza) - len(lista_przeciwnika)
    # lista krotek (cordy_pionka, cordy_docelowe, wynik, cordy_zbitego)
    min_max_value = None
    if kolor == Kolor.czarny:
        for cordy_pionka, cordy_docelowe, cordy_zbitego in mozliwe_ruchy_wszystkich_pionkow:
            nowa_lista_czarnych = przesun_pionek_na_liscie(lista_gracza, cordy_pionka, cordy_docelowe)
            if cordy_zbitego != 0:
                nowa_lista_bialych = usun_pionek_z_listy(lista_przeciwnika, cordy_zbitego)
            else:
                nowa_lista_bialych = lista_przeciwnika
            wynik_rekurencji = _ai_rek(nowa_lista_bialych, nowa_lista_czarnych, Kolor.bialy, deep)
            min_max_value = max_wynik(min_max_value, wynik_rekurencji)
    elif kolor == Kolor.bialy:
        for cordy_pionka, cordy_docelowe, cordy_zbitego in mozliwe_ruchy_wszystkich_pionkow:
            nowa_lista_bialych = przesun_pionek_na_liscie(lista_przeciwnika, cordy_pionka, cordy_docelowe)
            if cordy_zbitego != 0:
                nowa_lista_czarnych = usun_pionek_z_listy(lista_gracza, cordy_zbitego)
            else:
                nowa_lista_czarnych = lista_gracza
            wynik_rekurencji = _ai_rek(nowa_lista_bialych, nowa_lista_czarnych, Kolor.czarny, deep)
            min_max_value = min_wynik(min_max_value, wynik_rekurencji)
    return min_max_value


def znajdz_wszelkie_mozliwe_ruchy(lista_bialych, lista_czarnych, kolor):
    mozliwe_ruchy_wszystkich_pionkow = list()  # najlpsze ruchy kazdego pionka

    if kolor == Kolor.czarny:
        lista_pionkow_gracza = lista_czarnych
    elif kolor == Kolor.bialy:
        lista_pionkow_gracza = lista_bialych
    else:
        raise ValueError("Bledny kolor:  Kolor "+str(kolor))

    for foo in lista_pionkow_gracza:  # foo - coordynaty kazdego czarnego pionka
        mozliwe_ruchy_foo = mozliwe_ruchy(foo, kolor, lista_bialych, lista_czarnych)
        for ruch in mozliwe_ruchy_foo.items():
            mozliwe_ruchy_wszystkich_pionkow.append((foo, ruch[0], ruch[1]))
    return mozliwe_ruchy_wszystkich_pionkow


def random_max_ruch(mozliwe_ruchy_wszystkich_pionkow):
    maxim = None
    for pole_pionka, pole_docelowe, zbite_pionki, zbite_pole in mozliwe_ruchy_wszystkich_pionkow:
        if maxim < zbite_pionki:
            maxim = zbite_pionki
    ret_list = list()
    for pole_pionka, pole_docelowe, zbite_pionki, zbite_pole in mozliwe_ruchy_wszystkich_pionkow:
        if zbite_pionki == maxim:
            ret_list.append((pole_pionka, pole_docelowe, zbite_pole))
    if len(ret_list) != 0:
        return random.choice(ret_list)
    else:
        raise BrakMozliwegoRuchu