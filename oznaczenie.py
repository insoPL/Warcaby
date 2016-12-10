# -*- coding: utf-8 -*-
from tools import *
import pygame


class Oznaczenie(pygame.sprite.Sprite):
    def __init__(self, size, cords):
        pygame.sprite.Sprite.__init__(self)
        self.cords = cords
        self.size = size

        self.image, rect = load_png("oznaczenie.png")

        # Skaluj grafike oznaczenia
        self.image = pygame.transform.scale(self.image, size)

        self.move(*cords)

    def move(self, x, y):
        self.cords = (x, y)

    @property
    def rect(self):
        return pygame.Rect((self.cords[0] * self.size[0], (7 - self.cords[1]) * self.size[1]), self.size)
