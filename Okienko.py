# -*- coding: utf-8 -*-
from ObiektNaWierzchu import ObiektNaWierzchu
import pygame


class Okienko:
    def __init__(self, screen, cords):
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render('Hello World!', True, (255, 0, 0), (255, 255, 255))
        self.obiektNaWierzchu = ObiektNaWierzchu(screen, cords, text)
        self.obiektNaWierzchu.update()

    def update(self):
        self.obiektNaWierzchu.update()
