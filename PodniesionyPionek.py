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

        size = (size[0]+30, size[1]+30)  # powieksz go troche
        image = pygame.transform.scale(image, size)

        self.obiektNaWierzchu = ObiektNaWierzchu(screen, cords, image)

    def ukryj(self):
        self.obiektNaWierzchu.ukryj()

    def update(self):
        self.obiektNaWierzchu.przesun(pygame.mouse.get_pos())
