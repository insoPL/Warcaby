# -*- coding: utf-8 -*-


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
