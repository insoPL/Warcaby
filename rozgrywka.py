# -*- coding: utf-8 -*-
from tools import *
import pygame
import os
import sys
from pygame.locals import *



class Rozgrywka:
    """klasa reprezentujaca szachownice i calą jej zawartość"""
    def __init__(self, screen):
        self.screen = screen
        self.image, self.rect = load_png("szachownica.png")
        self.screen.blit(self.image, self.rect)

        self.pionki = list()  # lista wszystkich zawierajaca wszystkie pionki
        self.pionki.append(Pionek((self.rect.width/8, self.rect.height/8), (5, 5)))

        self.lista_pionkow = pygame.sprite.RenderPlain(self.pionki)  # Uchwyt slużący do renderowania pionków

        self.przenoszenie = -1

    def update(self):
        self.lista_pionkow.update()
        self.lista_pionkow.draw(self.screen)

    def click(self, pos):
        debug("[klik]: ", pos)
        if self.przenoszenie != -1:
            debug("[klik]: odlozenie!")
            self.screen.blit(self.image, self.przenoszenie.rect, self.przenoszenie.rect)
            self.przenoszenie.move(pos[0]/(self.rect.width/8), pos[1]/(self.rect.height/8))
            self.przenoszenie = -1
            self.update()

        else:
            for pionek in self.pionki:
                if pionek.rect.collidepoint(pos):
                    debug("[klik]: przenoszenie!")
                    self.przenoszenie = pionek

    def przesun_pionek(self, pionek):
        pionek.move(2, 2)


class Pionek(pygame.sprite.Sprite):
    def __init__(self,  size, cords):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_png("pionek.png")

        # Skaluj pionek
        self.image = pygame.transform.scale(self.image, size)
        self.rect.width, self.rect.height = size
        self.rect.width
        self.move(*cords)

    def move(self, x, y):
        self.rect.x = x * self.rect.width
        self.rect.y = y * self.rect.height
