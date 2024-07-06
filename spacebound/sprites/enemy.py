import pygame
import spacebound.globals as gl
from .laser import Laser
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None):
        super().__init__()
        self.image = pygame.image.load(gl.enemy_path)
        self.image_blast = pygame.image.load(gl.laser_green_blast_path)
        self.rect = self.image.get_rect()
        self.init_pos(x, y)
        self.rect.center = [self.x, self.y]
        self.fire_ready = True
        self.cooldown = 1000
        self.last_fired = 0
        self.destroy = False
        self.blast_counter = 5
        self.gap = 5

    def init_pos(self, x, y):
        if not x:
            self.x = random.randint(0, gl.window_width)
        else:
            self.x = x
        if not y:
            self.y = -int(gl.window_height * 0.1)
        else:
            self.y = y

    def move(self, target, meteor_group):
        meteor_corners = []
        for meteor in meteor_group:
            if meteor.rect.top < self.rect.bottom:
                meteor_corners.append([meteor.rect.left, meteor.rect.top])
                meteor_corners.append([meteor.rect.right, meteor.rect.top])
                meteor_corners.append([meteor.rect.left, meteor.rect.bottom])
                meteor_corners.append([meteor.rect.right, meteor.rect.bottom])

        left = max([cord[0] for cord in meteor_corners if cord[0] < self.x] + [0])
        right = min(
            [cord[0] for cord in meteor_corners if cord[0] > self.x] + [gl.window_width]
        )

        tx, ty = target

        if left > self.rect.left - self.gap:
            tx = self.rect.right
        if right < self.rect.right + self.gap:
            tx = self.rect.left

        speed = int(gl.speed * 0.7)
        dx = 0
        if self.x - tx < 0:
            dx = speed
        if self.x - tx > 0:
            dx = -speed
        if self.y > ty:
            dy = -gl.speed
        if self.y < ty:
            dy = gl.speed
        if abs(self.x - tx) < 2:
            dx = 0
        if abs(self.y - ty) < 2:
            dy = 0
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

    def update(self, target, meteor_group):
        if self.destroy:
            self.image = self.image_blast
            self.rect = self.image.get_rect()
            self.rect.center = [self.x, self.y]
            if self.blast_counter == 0:
                self.kill()
            self.blast_counter -= 1
        else:
            self.move(target, meteor_group)
            self.rect.center = [self.x, self.y]
