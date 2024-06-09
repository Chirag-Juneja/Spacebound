import pygame


class Background:
    def __init__(self, bg_path, win_h, speed=5):
        self.bg = pygame.image.load(bg_path).convert()
        self.h = self.bg.get_height()
        self.speed = speed
        self.win_h = win_h
        self.scroll = self.win_h - self.h

    def update(self, screen):
        screen.blit(self.bg, (0, self.scroll))

        if self.scroll > 0:
            screen.blit(self.bg, (0, self.scroll - self.h))

        if self.scroll > self.win_h:
            self.scroll = self.win_h - self.h

        self.scroll += self.speed
