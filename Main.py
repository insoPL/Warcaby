# -*- coding: utf-8 -*-

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
except ImportError, err:
    print "couldn't load module. %s" % (err)
    sys.exit(2)


def debug(foo):
    if hasattr(foo, "__str__"):
        print str(foo)
    else:
        print foo.__class__.__name__


def load_png(name):  # --> Surface, Rect
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Nie mozna wczytac:', fullname
        raise SystemExit, message
    return image, image.get_rect()


class Rozgrywka:
    """klasa reprezentujaca szachownice i calą jej zawartość"""
    def __init__(self):
        self.image, self.rect = load_png("szachownica.png")

        pionki = list()
        pionki.append(Pionek((5, 5), (self.rect.width/8, self.rect.height/8)))

        for foo in pionki:
            self.lista_pionkow = pygame.sprite.RenderPlain(foo)

        render_queue.append(self)

    def update(self):
        self.lista_pionkow.update()
        self.lista_pionkow.draw(screen)

    def click(self, pos):
        debug("klik")

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
        self.rect.y = (7-y) * self.rect.height


def main():
    global render_queue
    global screen
    render_queue = []  # kolejka obiektow czekajacy na renderowanie

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Warcaby')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    background.blit(*load_png("tlo.png"))
    render_queue.append(background)

    # Inicalizuj szachownice

    glowna_Rozgrywka = Rozgrywka()

    # Wyrenderuj wszystkie nie ruchome elementy do (Surface) screen
    for render in render_queue:
        if isinstance(render, pygame.Surface):
            debug(render)
            screen.blit(render, (0, 0))
        elif isinstance(render, tuple) and isinstance(render[0], pygame.Surface) and isinstance(render[1], pygame.Rect):
            debug(render)
            screen.blit(render[0], render[1])
        else:
            debug(render)
            screen.blit(render.image, render.rect)

    # renderuj zawartosc szachownicy
    glowna_Rozgrywka.update()

    # pierwsza klatka
    pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()

    # Event loop
    while True:
        # ograniczenie klatek na sekunde
        clock.tick(24)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN and glowna_Rozgrywka.rect.collidepoint(event.pos):
                glowna_Rozgrywka.click(event.pos)
        pygame.display.flip()

if __name__ == '__main__':
    main()
