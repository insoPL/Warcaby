# -*- coding: utf-8 -*-
from tools import *
import pygame


class Pionek(pygame.sprite.Sprite):
    def __init__(self,  size, cords, color):
        pygame.sprite.Sprite.__init__(self)

        self.color = color
        self.cords = cords

        self.size = size
        if color == Kolor.czarny:
            self.image, rect = load_png("pionek_czarny.png")
        elif color == Kolor.bialy:
            self.image, rect = load_png("pionek_bialy.png")
        else:
            raise ValueError

        # Skaluj pionek
        self.image = pygame.transform.scale(self.image, size)
        self.move(*cords)

    @property
    def rect(self):
        return pygame.Rect((self.cords[0]*self.size[0], (7-self.cords[1])*self.size[1]), self.size)

    def move(self, x, y):
        self.cords = (x, y)
