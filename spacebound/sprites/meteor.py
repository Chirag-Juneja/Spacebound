import pygame
from pathlib import Path
from random import randint


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for path in Path("./assets/meteors/").iterdir():
            self.images.append(pygame.image.load(path))
        idx = randint(0, len(self.images))
        self.image = self.images[idx]
        self.rect = self.image.get_rect()
        self.rect.center = [randint(0, 1024), randint(0, 100)]
