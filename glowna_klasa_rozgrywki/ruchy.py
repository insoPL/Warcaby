# -*- coding: utf-8 -*-
from tools import *


def mozliwe_ruchy(cords, color, biale, czarne):  # zwraca słownik dict[docelowy_cord] = zbity_pion
    return_dict = dict()
    if color == Color.white:  # jesli pionek jest bialy
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
    elif color == Color.black:
        if (cords[0]-1, cords[1]-1) not in czarne + biale:  # zwykly ruch
            if cords[0]-1 >= 0 and cords[1]-1 >= 0:
                return_dict[(cords[0]-1, cords[1]-1)] = 0

        if (cords[0]+1, cords[1]-1) not in czarne + biale:  # zwykly ruch
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
