import pygame
from pathlib import Path
from random import randint


class Meteor(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        paths = list(Path("./assets/meteors/").iterdir())
        idx = randint(0, len(paths)-1)
        self.image = pygame.image.load(paths[idx])
        self.rect = self.image.get_rect()
        self.rect.center = [randint(0, 1024), randint(0, 0)]
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
