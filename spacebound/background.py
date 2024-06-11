import pygame
import spacebound.globals as gl


class Background:
    def __init__(self):
        self.bg = pygame.image.load(gl.bg_path).convert()
        self.h = self.bg.get_height()
        self.w = self.bg.get_width()
        self.speed = gl.speed
        self.scroll = gl.window_height - self.h

    def update(self, screen):
        screen.blit(self.bg, (0, self.scroll))
        win_h = gl.window_height

        if self.scroll > 0:
            screen.blit(self.bg, (0, self.scroll - self.h))

        if self.scroll > win_h:
            self.scroll = win_h - self.h

        self.scroll += self.speed
