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


def debug(*args):
    for foo in args:
        if hasattr(foo, "__str__"):
            print str(foo),
        else:
            print foo.__class__.__name__,
    print


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
        render_queue.append(self)  # renderuj statyczne elementy

        self.pionki = list()  # lista wszystkich zawierajaca wszystkie pionki
        self.pionki.append(Pionek((self.rect.width/8, self.rect.height/8), (5, 5)))

        self.lista_pionkow = pygame.sprite.RenderPlain(self.pionki)  # Uchwyt slużący do renderowania pionków

        self.przenoszenie = -1

    def update(self):
        self.lista_pionkow.update()
        self.lista_pionkow.draw(screen)

    def click(self, pos):
        debug("[klik]: ", pos)
        if self.przenoszenie != -1:
            debug("[klik]: odlozenie!")
            screen.blit(staticbackground, self.przenoszenie.rect, self.przenoszenie.rect)
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


def main():
    global render_queue
    global screen
    global staticbackground
    render_queue = []  # kolejka obiektow czekajacy na renderowanie

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Warcaby')

    # Fill staticbackground
    staticbackground = pygame.Surface(screen.get_size())
    staticbackground = staticbackground.convert()
    staticbackground.fill((0, 0, 0))
    staticbackground.blit(*load_png("tlo.png"))

    # Inicalizuj szachownice

    glowna_rozgrywka = Rozgrywka()

    # Wyrenderuj wszystkie nie ruchome elementy do (Surface) staticbackground
    for render in render_queue:
        if isinstance(render, pygame.Surface):
            debug("[static render]:", render)
            staticbackground.blit(render, (0, 0))
        elif isinstance(render, tuple) and isinstance(render[0], pygame.Surface) and isinstance(render[1], pygame.Rect):
            debug("[static render]:", render)
            staticbackground.blit(render[0], render[1])
        else:
            debug("[static render]:", render)
            staticbackground.blit(render.image, render.rect)

    screen.blit(staticbackground, (0, 0))

    # renderuj zawartosc szachownicy
    glowna_rozgrywka.update()

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
            if event.type == MOUSEBUTTONDOWN and glowna_rozgrywka.rect.collidepoint(event.pos):
                glowna_rozgrywka.click(event.pos)
            if event.type == MOUSEBUTTONUP and glowna_rozgrywka.rect.collidepoint(event.pos) and glowna_rozgrywka.przenoszenie != -1:
                glowna_rozgrywka.click(event.pos)
        pygame.display.flip()

if __name__ == '__main__':
    main()
