# -*- coding: utf-8 -*-
from tools import *
import pygame



class Rozgrywka:
    """klasa reprezentujaca szachownice i calą jej zawartość"""
    def __init__(self, screen):
        self.screen = screen
        self.image, self.rect = load_png("szachownica.png")
        self.screen.blit(self.image, self.rect)

        self.pionki = list()  # lista zawierajaca wszystkie pionki

        for foo in range(0, 8, 2):  # dodaj pionki
            self.pionki.append(Pionek((self.rect.width/8, self.rect.height/8), (foo, 7), 0))  # czarne - dol ekranu
            self.pionki.append(Pionek((self.rect.width/8, self.rect.height/8), (foo+1, 6), 0))

            self.pionki.append(Pionek((self.rect.width/8, self.rect.height/8), (foo, 1), 1))  # biale
            self.pionki.append(Pionek((self.rect.width/8, self.rect.height/8), (foo+1, 0), 1))

        self.renderuj_pionki = pygame.sprite.RenderPlain(self.pionki)  # Uchwyt slużący do renderowania pionków

        self.przenoszenie = -1

    def update(self):
        self.renderuj_pionki.update()
        self.renderuj_pionki.draw(self.screen)

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
                debug(mozliwe_ruchy(pionek, self.pionki))

        elif pionek.color == 1:
            if oy == y-1 and (ox == x-1 or ox == x+1):
                pionek.move(x, y)


def czy_jest_na_polu(x, y, pionki):
    if x > 7 or y > 7 or x < 0 or y < 0:
        return -1
    for foo in pionki:
        if foo.getpos() == (x, y):
            return 1
    return 0


def mozliwe_ruchy(pionek, arg_pionki):  # mozliwe ruchy dla pionka z dana liczba pionkow
    kopia_pionki = list(arg_pionki)
    kopia_pionki.remove(pionek)

    zwracana_lista = list()
    pos = pionek.getpos()
    debug("pozycja", pos)
    if czy_jest_na_polu(pos[0]-1, pos[1]-1, kopia_pionki) == 1 and czy_jest_na_polu(pos[0]-2, pos[1]-2, kopia_pionki) == 0:
        # Przeciwnik na lewo do przodu i wolne miejsce za nim: mozna bic!

        debug("bij lewaka")
        zwracana_lista.append((pos[0]-2, pos[1]-2)) == 1
    if czy_jest_na_polu(pos[0]+1, pos[1]-1, kopia_pionki) and czy_jest_na_polu(pos[0]+2, pos[1]-2, kopia_pionki) == 0:
        # Przeciwnik na prawo do przodu i wolne miejsce za nim: mozna bic!
        zwracana_lista.append((pos[0]+2, pos[1]-2))
        debug("bij prawaka")
    return zwracana_lista

class ProstyPionek:
    def __init__(self, cords, color):
        self.color = color
        self.cords = cords

    def move(self, x, y):
        self.cords = (x, y)


class Pionek(ProstyPionek, pygame.sprite.Sprite):
    def __init__(self,  size, cords, color): # color 0-black 1-white
        pygame.sprite.Sprite.__init__(self)
        ProstyPionek.__init__(self, cords, color)
        self.size = size

        self.image, rect = load_png("pionek.png")

        # Skaluj pionek
        self.image = pygame.transform.scale(self.image, size)
        self.move(*cords)

    @property
    def rect(self):
        return pygame.Rect((self.cords[0]*self.size[0], self.cords[1]*self.size[1]), self.size)

    def getpos(self):
        return self.rect.x/self.rect.width, self.rect.y/self.rect.height
