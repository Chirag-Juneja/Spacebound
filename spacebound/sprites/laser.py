import pygame
from pathlib import Path
import spacebound.globals as gl


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, direction: bool = 0):
        super().__init__()
        # pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(gl.laster_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        speed = gl.speed*4
        if not self.direction:
            speed = -speed
        self.rect.y += speed
        if self.rect.bottom < 0:
            self.kill()
