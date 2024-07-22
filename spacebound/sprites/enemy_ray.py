import pygame
import spacebound.globals as gl
from .enemy import Enemy


class EnemyRay(Enemy):
    def __init__(self, x=None, y=None):
        super().__init__(x, y)
        self.image = pygame.image.load(gl.enemy_ray_path)
