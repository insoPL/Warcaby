# -*- coding: utf-8 -*-
import pygame


class ObiektNaWierzchu(pygame.sprite.RenderPlain):
    def __init__(self, screen, cords, image):
        self.onw = _ObiektNaWierzchu(cords, image)
        super(pygame.sprite.RenderPlain, self).__init__()
        self.add(self.onw)
        self.nadpisany_fragment_ekranu = None
        self.screen = screen
        self.stary_screen = screen.copy()

    def update(self):
        self.ukryj()
        self.stary_screen = self.screen.copy()
        self.draw(self.screen)

    def przesun(self, cords):
        self.onw.move(*cords)
        self.update()

    def ukryj(self):
        self.screen.blit(self.stary_screen, self.onw.rect, self.onw.rect)

    @property
    def rect(self):
        return self.onw.rect


class _ObiektNaWierzchu(pygame.sprite.Sprite):
    def __init__(self, cords, image):
        pygame.sprite.Sprite.__init__(self)

        self.cords = cords
        self.size = image.get_size()
        self.image = image
        self.rect = image.get_rect()

        # Skaluj onw
        self.move(*cords)

    def move(self, x, y):
        self.rect.center = (x, y)
