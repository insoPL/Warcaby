# -*- coding: utf-8 -*-

try:
    from socket import *
    from pygame.locals import *
    from tools import *
    from rozgrywka import *
except ImportError, err:
    print "couldn't load module. %s" % (err)
    sys.exit(2)


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Warcaby')
    pygame.display.set_icon(load_png("pionek.png")[0])

    # Fill background
    staticbackground = pygame.Surface(screen.get_size())
    staticbackground = staticbackground.convert()
    staticbackground.fill((0, 0, 0))
    staticbackground.blit(*load_png("tlo.png"))

    screen.blit(staticbackground, (0, 0))

    # Inicalizuj szachownice

    glowna_rozgrywka = Rozgrywka(screen)

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
