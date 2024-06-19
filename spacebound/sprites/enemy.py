import pygame
import spacebound.globals as gl
from .laser import Laser
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(gl.enemy_path)
        self.image_blast = pygame.image.load(gl.laser_green_blast_path)
        self.rect = self.image.get_rect()
        self.x = random.randint(0, gl.window_width)
        self.y = -int(gl.window_height * 0.1)
        self.rect.center = [self.x, self.y]
        self.fire_ready = True
        self.cooldown = 500
        self.last_fired = 0
        self.destroy = False
        self.blast_counter = 5

    def move(self, target):
        tx, ty = target
        speed = int(gl.speed * 0.5)
        dx = 0
        if self.x - tx < 0:
            dx = speed
        if self.x - tx > 0:
            dx = -speed
        if self.y > gl.window_height * 0.2:
            dy = 0
        else:
            dy = gl.speed
        self.x += dx
        self.y += dy

    def fire(self):
        if self.destroy:
            return

        now = pygame.time.get_ticks()

        if now - self.last_fired >= self.cooldown:
            self.fire_ready = True

        if self.fire_ready:
            self.fire_ready = False
            self.last_fired = pygame.time.get_ticks()
            laser = Laser(self.x, self.y, 1, "Green")
            return laser

    def update(self, target):
        if self.destroy:
            self.image = self.image_blast
            self.rect = self.image.get_rect()
            self.rect.center = [self.x, self.y]
            if self.blast_counter == 0:
                self.kill()
            self.blast_counter -= 1
        else:
            self.move(target)
            self.rect.center = [self.x, self.y]
