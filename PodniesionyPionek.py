# -*- coding: utf-8 -*-
from tools import *
from ObiektNaWierzchu import ObiektNaWierzchu

class PodniesionyPionek:
    def __init__(self, screen, size, cords, color):
        if color == Kolor.czarny:
            image, rect = load_png("pionek_czarny.png")
        elif color == Kolor.bialy:
            image, rect = load_png("pionek_bialy.png")
        else:
            raise ValueError

        self.obiektNaWierzchu = ObiektNaWierzchu(screen, size, cords, image, rect)

    def ukryj(self):
        self.obiektNaWierzchu.ukryj()

    def update(self):
        self.obiektNaWierzchu.update()