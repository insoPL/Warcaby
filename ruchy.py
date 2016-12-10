# -*- coding: utf-8 -*-
from tools import *


def mozliwe_ruchy(cords, color, biale, czarne):  # zwraca słownik dict[docelowy_cord] = zbity_pion
    return_dict = dict()
    if color == 1:  # jesli pionek jest bialy
        if (cords[0]-1, cords[1]+1) not in czarne + biale:  # zwykly ruch
            if cords[0]-1 >= 0 and cords[1]+1 <= 7:
                return_dict[(cords[0]-1, cords[1]+1)] = 0

        if (cords[0]+1, cords[1]+1) not in czarne + biale:  # zwykly ruch
            if cords[0]+1 <= 7 and cords[1]+1 <= 7:
                return_dict[(cords[0]+1, cords[1]+1)] = 0

        if (cords[0] - 1, cords[1] + 1) in czarne and (cords[0] - 2, cords[1] + 2) not in czarne + biale:
            # Ruch bicia
            if cords[0] - 2 >= 0 and cords[1] + 2 <= 7:
                return_dict[(cords[0] - 2, cords[1] + 2)] = (cords[0] - 1, cords[1] + 1)

        if (cords[0] + 1, cords[1] + 1) in czarne and (cords[0] + 2, cords[1] + 2) not in czarne + biale:
            # Ruch bicia
            if cords[0]+2 <= 7 and cords[1]+2 <= 7:
                return_dict[(cords[0] + 2, cords[1] + 2)] = (cords[0] + 1, cords[1] + 1)
    if color == 0:
        if (cords[0]-1, cords[1]-1) not in czarne + biale:  # zwykly ruch
            if cords[0]-1 >= 0 and cords[1]-1 >= 0:
                return_dict[(cords[0]-1, cords[1]-1)] = 0

        if (cords[0]+1, cords[1]-1) not in czarne + biale:  # zwykly ruch7
            if cords[0]+1 <= 7 and cords[1]-1 >= 0:
                return_dict[(cords[0]+1, cords[1]-1)] = 0

        if (cords[0]+1, cords[1]-1) in biale and (cords[0]+2, cords[1]-2) not in czarne + biale:
            # Ruch bicia
            if cords[0]+2 <= 7 and cords[1]-2 >= 0:
                return_dict[(cords[0]+2, cords[1]-2)] = (cords[0]+1, cords[1]-1)
        if (cords[0]-1, cords[1]-1) in biale and (cords[0]-2, cords[1]-2) not in czarne + biale:
            # Ruch bicia
            if cords[0]-2 >= 0 and cords[1]-2 >= 0:
                return_dict[(cords[0]-2, cords[1]-2)] = (cords[0]-1, cords[1]-1)
    return return_dict


# #####################################################################juz nie używane

def jaki_kolor_jest_na_polu(x, y, pionki):
    if x > 7 or y > 7 or x < 0 or y < 0:
        return -1
    for foo in pionki.keys():
        if foo == (x, y):
            return pionki[foo]
    return


def znajdz_bitego(pos1, pos2):
    if pos1[1] - pos2[1] == -2:  # jesli biale
        if pos1[0] - pos2[0] == 2:
            return pos1[0] - 1, pos1[1] + 1
        elif pos1[0] - pos2[0] == -2:
            return pos1[0] + 1, pos1[1] + 1
    if pos1[1] - pos2[1] == 2:  # jesli czarne
        if pos1[0] - pos2[0] == 2:
            return pos1[0] - 1, pos1[1] - 1
        elif pos1[0] - pos2[0] == -2:
            return pos1[0] + 1, pos1[1] - 1
    return 0
