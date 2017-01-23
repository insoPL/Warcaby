# -*- coding: utf-8 -*-
from tools import *
import pygame


class PodniesionyPionek(pygame.sprite.RenderPlain):
    def __init__(self, screen, size, cords, color):
        self.pionek = _PodniesionyPionek(size, cords, color)
        super(pygame.sprite.RenderPlain, self).__init__()
        self.add(self.pionek)
        self.nadpisany_fragment_ekranu = None
        self.screen = screen
        self.stary_screen = screen.copy()

    def update(self):
        self.ukryj()
        self.stary_screen = self.screen.copy()
        self.pionek.move(*pygame.mouse.get_pos())
        self.draw(self.screen)

    def ukryj(self):
        self.screen.blit(self.stary_screen, self.pionek.rect, self.pionek.rect)

class _PodniesionyPionek(pygame.sprite.Sprite):
    def __init__(self,  size, cords, color):
        pygame.sprite.Sprite.__init__(self)

        self.color = color
        self.cords = cords
        self.size = size
        if color == Kolor.czarny:
            self.image, self.rect = load_png("pionek_czarny.png")
        elif color == Kolor.bialy:
            self.image, self.rect = load_png("pionek_bialy.png")
        else:
            raise ValueError

        # Skaluj pionek
        self.image = pygame.transform.scale(self.image, size)
        self.move(*cords)

    def move(self, x, y):
        self.rect.center = (x, y)
