# -*- coding: utf-8 -*-
from ObiektNaWierzchu import ObiektNaWierzchu
from pygame.locals import *
from tools import *


def wyswietl_zapytanie_o_tryb_gry(screen):
    okienko = Zapytanie(screen, screen.get_rect().center, (152, 50, 0), (0, 0, 0))
    clock = pygame.time.Clock()

    while True:
        clock.tick(20)
        okienko.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif okienko is not None and (
                    event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP) and (
                    okienko.rect.collidepoint(event.pos)):
                wynik = okienko.on_click(event.pos)
                if wynik:
                    return wynik-1
        pygame.display.flip()


class Zapytanie:
    def __init__(self, screen, cords, kolor_wypelnienia, kolor_czcionki):
        self.przyciski_rect = list()
        surface = pygame.Surface((500, 300))
        surface.fill(kolor_wypelnienia)

        self.dodaj_tekst(surface, "Wybierz Przeciwnika:", kolor_czcionki, kolor_wypelnienia, cords, 10)

        self.dodaj_przycisk(surface, "Gracz", kolor_czcionki, 80)
        self.dodaj_przycisk(surface, "AI", kolor_czcionki, -80)

        self.obiektNaWierzchu = ObiektNaWierzchu(screen, cords, surface)
        self.obiektNaWierzchu.update()

    def dodaj_przycisk(self, surface, tekst, kolor_czcionki, wychylenie_wzgledem_osii_symetri):
        rozmiar_przycisku = (100, 60)
        przycisk = pygame.Surface(rozmiar_przycisku)
        przycisk.fill((255, 255, 255))
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render(tekst, True, kolor_czcionki, (255, 255, 255))
        rect = przycisk.get_rect()
        rect.move_ip(rozmiar_przycisku[0] / 2 - text.get_size()[0] / 2, 10)
        self.przyciski_rect.append(rect)
        przycisk.blit(text, rect)
        surf_rect = surface.get_rect()
        rect.move_ip(surf_rect.centerx - przycisk.get_rect().width / 2 - wychylenie_wzgledem_osii_symetri,
                     surf_rect.bottom - przycisk.get_size()[1]-20)
        surface.blit(przycisk, rect)

    def dodaj_tekst(self, surface, tekst, kolor_czcionki, kolor_wypelnienia, cords, poziom):
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render(tekst, True, kolor_czcionki, kolor_wypelnienia)
        rect = surface.get_rect()
        rect.move_ip(surface.get_size()[0] / 2 - text.get_size()[0] / 2, poziom)
        surface.blit(text, rect)
        self.cords = (cords[0] - surface.get_size()[0] / 2, cords[1] - surface.get_size()[1] / 2)

    def update(self):
        self.obiektNaWierzchu.update()

    def on_click(self, cords):
        cords = (cords[0] - self.cords[0], cords[1] - self.cords[1])

        for x in xrange(len(self.przyciski_rect)):
            debug(self.przyciski_rect[x], cords)
            if self.przyciski_rect[x].collidepoint(cords):
                return x+1
        return False

    @property
    def rect(self):
        return self.obiektNaWierzchu.rect
