# -*- coding: utf-8 -*-
import pygame


class ObiektNaWierzchu(pygame.sprite.RenderPlain):
    def __init__(self, screen, size, cords, image, rect):
        self.onw = _ObiektNaWierzchu(size, cords, image, rect)
        super(pygame.sprite.RenderPlain, self).__init__()
        self.add(self.onw)
        self.nadpisany_fragment_ekranu = None
        self.screen = screen
        self.stary_screen = screen.copy()

    def update(self):
        self.ukryj()
        self.stary_screen = self.screen.copy()
        self.onw.move(*pygame.mouse.get_pos())
        self.draw(self.screen)

    def ukryj(self):
        self.screen.blit(self.stary_screen, self.onw.rect, self.onw.rect)


class _ObiektNaWierzchu(pygame.sprite.Sprite):
    def __init__(self,  size, cords, image, rect):
        pygame.sprite.Sprite.__init__(self)

        self.cords = cords
        self.size = size
        self.image = image
        self.rect = rect

        # Skaluj onw
        self.image = pygame.transform.scale(self.image, size)
        self.move(*cords)

    def move(self, x, y):
        self.rect.center = (x, y)
