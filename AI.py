# -*- coding: utf-8 -*-
from tools import *
from ruchy import *
import random

# czarne to AI


def ai(lista_bialych, lista_czarnych):  # --> coordy najlepszego ruchu
    deep = 2
    return ai_rek(lista_bialych, lista_czarnych, deep)


def ai_rek(lista_bialych, lista_czarnych, deep):  # zwraca (skad, dokad, ile_zbije)
    if deep == 0:
        return dict()
    deep -= 1  # ogranicznik głębokości

    # ################################### fragment budujacy
    najlepsze_ruchy = list()  # najlpsze ruchy kazdego pionka
    for foo in lista_czarnych:  # foo - coordynaty kazdego czarnego pionka
        ruchy = mozliwe_ruchy(foo, 0, lista_bialych, lista_czarnych)  # ruchy = dict[miejsce_docelowe] = (miejsce_zbite)
        # dla każdego możliwego ruchu tego pionka
        wyniki_ruchow_foo = dict()
        for ruch in ruchy.items():  # ruch = (docelowy, zbity)
            wyniki_ruchow_foo[ruch[0]] = 0
            if ruch[1] != 0:  # ruch bijacy
                # tu rekurencja zwiekszajaca wyniki_ruchow[ruch[0]]
                wyniki_ruchow_foo[ruch[0]] = 1
        # ################################### zwijanie rekurencji
        wynik_ruchu_foo = random_max_value(wyniki_ruchow_foo)  # najlepszy ruch pionkiem foo (docelowy, wynik)
        if wynik_ruchu_foo: najlepsze_ruchy.append((foo, wynik_ruchu_foo[0],wynik_ruchu_foo[1]))
    debug("najlepsze ruchy ", najlepsze_ruchy)
    najlepsze_wyniki = random_max_value2(najlepsze_ruchy)
    debug("najlepsze wyniki: ", najlepsze_wyniki)
