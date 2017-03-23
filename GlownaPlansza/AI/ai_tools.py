# -*- coding: utf-8 -*-
from tools import Kolor, BrakMozliwegoRuchu
from GlownaPlansza.ruchy import mozliwe_ruchy, mozliwe_bicia
import random


def znajdz_wszelkie_mozliwe_ruchy(lista_bialych, lista_czarnych, kolor):
    mozliwe_ruchy_wszystkich_pionkow = list()  # najlpsze ruchy kazdego pionka

    if kolor == Kolor.czarny:
        lista_pionkow_gracza = lista_czarnych
    elif kolor == Kolor.bialy:
        lista_pionkow_gracza = lista_bialych
    else:
        raise ValueError("Bledny kolor:  Kolor "+str(kolor))

    for foo in lista_pionkow_gracza:
        mozliwe_ruchy_foo = mozliwe_bicia(foo, kolor, lista_bialych, lista_czarnych)
        for ruch in mozliwe_ruchy_foo.items():
            mozliwe_ruchy_wszystkich_pionkow.append((foo, ruch[0], ruch[1]))
    if len(mozliwe_ruchy_wszystkich_pionkow) == 0:
        for foo in lista_pionkow_gracza:  # foo - coordynaty kazdego czarnego pionka
            mozliwe_ruchy_foo = mozliwe_ruchy(foo, kolor, lista_bialych, lista_czarnych)
            for ruch in mozliwe_ruchy_foo.items():
                mozliwe_ruchy_wszystkich_pionkow.append((foo, ruch[0], ruch[1]))
    return mozliwe_ruchy_wszystkich_pionkow


def random_max_ruch(mozliwe_ruchy_wszystkich_pionkow):
    maxim = None
    for pole_pionka, pole_docelowe, zbite_pionki, zbite_pola in mozliwe_ruchy_wszystkich_pionkow:
        if maxim < zbite_pionki:
            maxim = zbite_pionki
    ret_list = list()
    for pole_pionka, pole_docelowe, zbite_pionki, zbite_pola in mozliwe_ruchy_wszystkich_pionkow:
        if zbite_pionki == maxim:
            ret_list.append((pole_pionka, pole_docelowe, zbite_pola))
    if len(ret_list) != 0:
        return random.choice(ret_list)
    else:
        raise BrakMozliwegoRuchu


def max_wynik(best_value, this_value):
    if best_value is None:
        return this_value
    else:
        return max(best_value, this_value)


def min_wynik(best_value, this_value):
    if best_value is None:
        return this_value
    else:
        return min(best_value, this_value)


def przesun_pionek_na_liscie(lista, cordy_pionka, cordy_docelowe):
    ret_list = list()
    for pionek in lista:
        if pionek == cordy_pionka:
            ret_list.append(cordy_docelowe)
        else:
            ret_list.append(pionek)
    return ret_list


def usun_pionek_z_listy(lista, cordy_zbitego):
    ret_list = list()
    for pionek in lista:
        if pionek != cordy_zbitego:
            ret_list.append(pionek)
    return ret_list
