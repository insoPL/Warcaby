# -*- coding: utf-8 -*-
from tools import *

def mozliwe_ruchy(cords, color, biale, czarne):  # zwraca słownik dict[docelowy_cord] = zbity_pion
    return_dict = dict()
    if color == 1:  # jesli pionek jest bialy
        if (cords[0]-1, cords[1]+1) not in czarne + biale:  # zwykly ruch
            return_dict[(cords[0]-1, cords[1]+1)] = 0

        if (cords[0]+1, cords[1]+1) not in czarne + biale:  # zwykly ruch
            return_dict[(cords[0]+1, cords[1]+1)] = 0

        if (cords[0] - 1, cords[1] + 1) in czarne and (cords[0] - 2, cords[1] + 2) not in czarne + biale:
            # Ruch bicia
            return_dict[(cords[0] - 2, cords[1] + 2)] = (cords[0] - 1, cords[1] + 1)

        if (cords[0] + 1, cords[1] + 1) in czarne and (cords[0] + 2, cords[1] + 2) not in czarne + biale:
            # Ruch bicia
            return_dict[(cords[0] + 2, cords[1] + 2)] = (cords[0] + 1, cords[1] + 1)
    if color == 0:
        if (cords[0]-1, cords[1]-1) not in czarne + biale:  # zwykly ruch
            return_dict[(cords[0]-1, cords[1]-1)] = 0

        if (cords[0]+1, cords[1]-1) not in czarne + biale:  # zwykly ruch
            return_dict[(cords[0]+1, cords[1]-1)] = 0

        if (cords[0]+1, cords[1]-1) in biale and (cords[0]+2, cords[1]-2) not in czarne + biale:
            # Ruch bicia
            return_dict[(cords[0]+2, cords[1]-2)] = (cords[0]+1, cords[1]-1)
        if (cords[0]-1, cords[1]-1) in biale and (cords[0]-2, cords[1]-2) not in czarne + biale:
            # Ruch bicia
            return_dict[(cords[0]-2, cords[1]-2)] = (cords[0]-1, cords[1]-1)
    return return_dict


def jaki_kolor_jest_na_polu(x, y, pionki):
    if x > 7 or y > 7 or x < 0 or y < 0:
        return -1
    for foo in pionki.keys():
        if foo == (x, y):
            return pionki[foo]
    return -1
