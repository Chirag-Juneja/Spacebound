import pygame
import spacebound.globals as gl
from .laser import Laser
from .enemy import Enemy


class EnemyRay(Enemy):
    def __init__(self, x=None, y=None):
        super().__init__(x, y)
        self.image = pygame.image.load(gl.enemy_ray_path)
        self.points = 15
        self.fire_count = 0

    def fire(self):
        if self._destroy:
            return

        now = pygame.time.get_ticks()

        if now - self.last_fired >= self.cooldown:
            self.fire_ready = True

        if self.fire_ready:
            if self.fire_count > 10:
                self.fire_ready = False
                self.fire_count = 0
                self.last_fired = pygame.time.get_ticks()
            self.fire_count += 1
            laser = Laser(self.x, self.y, 1, "GreenBold")
            return laser
