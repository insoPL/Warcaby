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

        self.pionki = list()  # lista zawierajaca wszystkie pionki

        for foo in range(0, 8, 2):  # dodaj pionki
            self.pionki.append(Pionek((self.rect.width/8, self.rect.height/8), (foo, 7), 0))  # czarne
            self.pionki.append(Pionek((self.rect.width/8, self.rect.height/8), (foo+1, 6), 0))

            self.pionki.append(Pionek((self.rect.width/8, self.rect.height/8), (foo, 1), 1))  # biale
            self.pionki.append(Pionek((self.rect.width/8, self.rect.height/8), (foo+1, 0), 1))

        self.lista_pionkow = pygame.sprite.RenderPlain(self.pionki)  # Uchwyt slużący do renderowania pionków

        self.przenoszenie = -1

    def update(self):
        self.lista_pionkow.update()
        self.lista_pionkow.draw(self.screen)

    def click(self, pos):
        debug("[klik]: ", pos)
        if self.przenoszenie != -1:  # JEST w trybie przenoszenia
            debug("[klik]: odlozenie!")
            self.screen.blit(self.image, self.przenoszenie.rect, self.przenoszenie.rect)
            self.przesun_pionek(self.przenoszenie, pos[0]/(self.rect.width/8), pos[1]/(self.rect.height/8))
            self.przenoszenie = -1
            self.update()

        else:  # NIE jest w trybie przenoszenia
            for pionek in self.pionki:
                if pionek.rect.collidepoint(pos):
                    debug("[klik]: przenoszenie!")
                    self.przenoszenie = pionek

    def przesun_pionek(self, pionek, x, y):
        ox, oy = pionek.getpos()
        if pionek.color == 0:  # jesli pionek jest czarny
            if oy == y+1 and (ox == x-1 or ox == x+1):
                pionek.move(x, y)
        elif pionek.color == 1:
            if oy == y-1 and (ox == x-1 or ox == x+1):
                pionek.move(x, y)


class Pionek(pygame.sprite.Sprite):
    def __init__(self,  size, cords, color): # color 0-black 1-white
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_png("pionek.png")
        self.color = color

        # Skaluj pionek
        self.image = pygame.transform.scale(self.image, size)
        self.rect.width, self.rect.height = size
        self.rect.width
        self.move(*cords)

    def move(self, x, y):
        self.rect.x = x * self.rect.width
        self.rect.y = y * self.rect.height

    def getpos(self):
        return self.rect.x/self.rect.width, self.rect.y/self.rect.height