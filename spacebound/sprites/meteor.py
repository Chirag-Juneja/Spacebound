import pygame
from pathlib import Path
from random import randint
import spacebound.globals as gl


class Meteor(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        paths = list(Path(gl.meteor_path).iterdir())
        idx = randint(0, len(paths) - 1)
        self.image = pygame.image.load(paths[idx])
        self.rect = self.image.get_rect()
        self.rect.center = [randint(0, gl.window_width), -100]

    def update(self):
        self.rect.y += gl.speed
        if self.rect.top > gl.window_height:
            self.kill()
