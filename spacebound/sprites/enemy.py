import pygame
import spacebound.globals as gl
from .laser import Laser
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(gl.enemy_path)
        self.rect = self.image.get_rect()
        self.x = random.randint(0, gl.window_width)
        self.y = -int(gl.window_height*0.1)
        self.rect_center = [self.x, self.y]
        self.fire_ready = True
        self.cooldown = 500
        self.last_fired = 0

    def move(self, target):
        tx, ty = target
        dx = 0
        if self.x - tx < 0:
            dx = gl.speed
        if self.x - tx > 0:
            dx = -gl.speed
        if self.y > gl.window_height*0.2:
            dy = 0
        else:
            dy = gl.speed
        self.x += dx
        self.y += dy

    def fire(self):
        now = pygame.time.get_ticks()

        if now - self.last_fired >= self.cooldown:
            self.fire_ready = True

        if self.fire_ready:
            self.fire_ready = False
            self.last_fired = pygame.time.get_ticks()
            laser = Laser(self.x, self.y, 1, "Green")
            return laser

    def update(self, target):
        self.move(target)
        self.rect.center = [self.x, self.y]
