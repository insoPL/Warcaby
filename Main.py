# -*- coding: utf-8 -*-
from pygame.locals import *
from tools import *
from GlownaPlansza import GlownaPlansza
from PodniesionyPionek import PodniesionyPionek
from Okienko import Okienko


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Warcaby')
    pygame.display.set_icon(load_png("pionek_czarny.png")[0])

    # Fill background
    staticbackground = pygame.Surface(screen.get_size())
    staticbackground = staticbackground.convert()
    staticbackground.fill((0, 0, 0))
    staticbackground.blit(*load_png("tlo.png"))

    screen.blit(staticbackground, (0, 0))

    # Inicalizuj szachownice

    glowna_rozgrywka = GlownaPlansza(screen)

    # renderuj zawartosc szachownicy
    glowna_rozgrywka.update()

    # pierwsza klatka
    pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()
    podniesiony_pionek = None

    okienko = Okienko(screen, screen.get_rect().center)

    # Event loop
    while True:
        # ograniczenie klatek na sekunde
        clock.tick(20)
        okienko.update()

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if event.type == MOUSEBUTTONDOWN and glowna_rozgrywka.rect.collidepoint(event.pos):
                    glowna_rozgrywka.on_click(event.pos)
                if event.type == MOUSEBUTTONUP and glowna_rozgrywka.przesowany_pionek != -1:
                    glowna_rozgrywka.on_click(event.pos)
        except PodniesieniePionka as event:
            podniesiony_pionek = PodniesionyPionek(screen, glowna_rozgrywka.size_of_one_tile, pygame.mouse.get_pos(), event.kolor)
        except OpuszczeniePionka:
            podniesiony_pionek = None

        if podniesiony_pionek is not None:
            podniesiony_pionek.update()
        pygame.display.flip()
        if podniesiony_pionek is not None:
            podniesiony_pionek.ukryj()

if __name__ == '__main__':
    main()
