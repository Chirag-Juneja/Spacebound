import pygame
from pathlib import Path
import spacebound.globals as gl
import random


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        paths = list(Path(gl.meteor_path).iterdir())
        idx = random.randint(0, len(paths) - 1)
        self.image = pygame.image.load(paths[idx])
        self.rect = self.image.get_rect()
        options = [int(idx*gl.window_width*0.1) for idx in range(10)]
        x = random.choice(options)
        self.rect.center = [x, -100]

    def update(self):
        self.rect.y += gl.speed
        if self.rect.top > gl.window_height:
            self.kill()
