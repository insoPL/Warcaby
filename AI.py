# -*- coding: utf-8 -*-
from ruchy import *
import random


def ai(lista_bialych, lista_czarnych):
    mozliwe_ruchy_wszystkich_pionkow = znajdz_wszelkie_mozliwe_ruchy(lista_bialych, lista_czarnych, 0)
    wyniki = list()
    for cordy_pionka, cordy_docelowe, cordy_zbitego in mozliwe_ruchy_wszystkich_pionkow:
        nowa_lista_czarnych = move(lista_czarnych, cordy_pionka, cordy_docelowe)
        if cordy_zbitego != 0:
            nowa_lista_bialych = usun_pionek(lista_bialych, cordy_zbitego)
        else:
            nowa_lista_bialych = lista_bialych
        deep = 4
        wynik = ai_rek(nowa_lista_bialych, nowa_lista_czarnych, 1, deep)

        wyniki.append((cordy_pionka, cordy_docelowe, wynik, cordy_zbitego))
        debug("wynik dla", cordy_pionka, "->", cordy_docelowe,": ", wynik)
    return random_max_ruch(wyniki)


def ai_rek(lista_bialych, lista_czarnych, color,  deep):  # zwraca (skad, dokad, ile_zbije, co_zbije)
    if deep == 0:
        return len(lista_czarnych) - len(lista_bialych)
    deep -= 1  # ogranicznik głębokości

    mozliwe_ruchy_wszystkich_pionkow = znajdz_wszelkie_mozliwe_ruchy(lista_bialych, lista_czarnych, color)

    if len(mozliwe_ruchy_wszystkich_pionkow) == 0:
        return len(lista_czarnych) - len(lista_bialych)
    # lista krotek (cordy_pionka, cordy_docelowe, wynik, cordy_zbitego)
    min_max_value = None
    if color == Color.black:
        for cordy_pionka, cordy_docelowe, cordy_zbitego in mozliwe_ruchy_wszystkich_pionkow:
            nowa_lista_czarnych = move(lista_czarnych, cordy_pionka, cordy_docelowe)
            if cordy_zbitego != 0:
                nowa_lista_bialych = usun_pionek(lista_bialych, cordy_zbitego)
            else:
                nowa_lista_bialych = lista_bialych
            min_max_value = max_wynik(min_max_value, ai_rek(nowa_lista_bialych, nowa_lista_czarnych, 1, deep))
    elif color == Color.white:
        for cordy_pionka, cordy_docelowe, cordy_zbitego in mozliwe_ruchy_wszystkich_pionkow:
            nowa_lista_bialych = move(lista_bialych, cordy_pionka, cordy_docelowe)
            if cordy_zbitego != 0:
                nowa_lista_czarnych = usun_pionek(lista_czarnych, cordy_zbitego)
            else:
                nowa_lista_czarnych = lista_czarnych
            mini =ai_rek(nowa_lista_bialych, nowa_lista_czarnych, 0, deep)
            min_max_value = min_wynik(min_max_value, mini)
    return min_max_value


def max_wynik(best_value, this_value):
    if best_value is None:
        return this_value
    elif best_value < this_value:
        return this_value
    else:
        return best_value


def min_wynik(best_value, this_value):
    if best_value is None:
        return this_value
    elif best_value > this_value:
        return this_value
    else:
        return best_value


def move(lista, cordy_pionka, cordy_docelowe):
    ret_list = list()
    for pionek in lista:
        if pionek == cordy_pionka:
            ret_list.append(cordy_docelowe)
        else:
            ret_list.append(pionek)
    return ret_list


def usun_pionek(lista, cordy_zbitego):
    ret_list = list()
    for pionek in lista:
        if pionek != cordy_zbitego:
            ret_list.append(pionek)
    return ret_list


def znajdz_wszelkie_mozliwe_ruchy(lista_bialych, lista_czarnych, color):
    mozliwe_ruchy_wszystkich_pionkow = list()  # najlpsze ruchy kazdego pionka

    if color == 0:
        for foo in lista_czarnych:  # foo - coordynaty kazdego czarnego pionka
            mozliwe_ruchy_foo = mozliwe_ruchy(foo, 0, lista_bialych, lista_czarnych)
            for ruch in mozliwe_ruchy_foo.items():
                mozliwe_ruchy_wszystkich_pionkow.append((foo, ruch[0], ruch[1]))
    elif color == 1:
        for foo in lista_bialych:  # foo - coordynaty kazdego czarnego pionka
            mozliwe_ruchy_foo = mozliwe_ruchy(foo, 1, lista_bialych, lista_czarnych)
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
