import pygame
from pathlib import Path
import spacebound.globals as gl


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, direction: bool = 0):
        super().__init__()
        # pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(gl.laser_path)
        self.image_blast = pygame.image.load(gl.laser_blast_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.hit = False
        self.blast_counter = 5

    def update(self):
        if self.hit:
            if self.blast_counter == 5:
                self.image = self.image_blast
                x, y = self.rect.x, self.rect.y
                self.rect = self.image.get_rect()
                self.rect.center = (x, y)
            if self.blast_counter == 0:
                self.kill()
            self.blast_counter -= 1
        else:
            speed = gl.speed*5
            if not self.direction:
                speed = -speed
            self.rect.y += speed
            if self.rect.bottom < 0:
                self.kill()
