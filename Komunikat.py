# -*- coding: utf-8 -*-
from ObiektNaWierzchu import ObiektNaWierzchu
from tools import *
from pygame.locals import *


def wyswietl_komunikat_o_wyniku_meczu(screen, kto_wygral):
    if kto_wygral == Kolor.bialy:
        tresc_komunikatu = "mecz wygral gracz bialy"
    elif kto_wygral == Kolor.czarny:
        tresc_komunikatu = "mecz wygral gracz czarny"
    else:
        raise ValueError

    okienko = Komunikat(screen, screen.get_rect().center, (152, 50, 0), (0, 0, 0), "Koniec gry", tresc_komunikatu)

    clock = pygame.time.Clock()

    while True:
        clock.tick(20)
        okienko.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif okienko is not None and (event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP) and okienko.rect.collidepoint(event.pos):
                if okienko.on_click(event.pos):
                    return
        pygame.display.flip()


class Komunikat:
    def __init__(self, screen, cords, kolor_wypelnienia, kolor_czcionki, *teksty):
        surface = pygame.Surface((500, 300))
        surface.fill(kolor_wypelnienia)

        wysokosc = 10
        for tekst in teksty:
            self.dodaj_tekst(surface, tekst, kolor_czcionki, kolor_wypelnienia, cords, wysokosc)
            wysokosc += 50

        rozmiar_przycisku = (100, 60)
        self.przycisk = pygame.Surface(rozmiar_przycisku)
        self.przycisk.fill((255, 255, 255))
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render("ok", True, kolor_czcionki, (255, 255, 255))
        rect = self.przycisk.get_rect()
        rect.move_ip(rozmiar_przycisku[0] / 2 - text.get_size()[0] / 2, 10)
        self.przycisk.blit(text, rect)

        rect = surface.get_rect()
        rect.move_ip(surface.get_rect().centerx - self.przycisk.get_rect().width/2, surface.get_rect().bottom-self.przycisk.get_size()[1]-10)
        self.przycisk_rect = rect
        surface.blit(self.przycisk, rect)

        self.obiektNaWierzchu = ObiektNaWierzchu(screen, cords, surface)
        self.obiektNaWierzchu.update()

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

        if self.przycisk_rect.collidepoint(cords):
            return True
        return False

    @property
    def rect(self):
        return self.obiektNaWierzchu.rect
