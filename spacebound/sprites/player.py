import pygame
import spacebound.globals as gl
from .laser import Laser


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(gl.player_path)
        self.rect = self.image.get_rect()
        self.x = int(gl.window_width / 2)
        self.y = gl.window_height - int(gl.window_height*0.1)
        self.rect.center = [self.x, self.y]
        self.fire_ready = True
        self.cooldown = 200
        self.last_fired = 0

    def move(self, dx=0, dy=0):
        if self.rect.left < 0 and dx < 0:
            dx = 0
        if self.rect.right > gl.window_width and dx > 0:
            dx = 0
        self.x += dx

        if self.rect.top < 0 and dy < 0:
            dy = 0
        if self.rect.bottom > gl.window_width and dy > 0:
            dy = 0
        self.y += dy

    def fire(self):
        now = pygame.time.get_ticks()

        if now - self.last_fired >= self.cooldown:
            self.fire_ready = True

        if self.fire_ready:
            self.fire_ready = False
            self.last_fired = pygame.time.get_ticks()
            laser = Laser(self.x, self.y, 0)
            return laser

    def update(self):
        self.rect.center = [self.x, self.y]
