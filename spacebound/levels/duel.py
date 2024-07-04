import pygame
from spacebound.sprites.enemy import Enemy


class Duel:
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.cooldown = 1000
        self.last_live_enemy = pygame.time.get_ticks()

    def create_enemy(self):
        now = pygame.time.get_ticks()
        if now - self.last_live_enemy > self.cooldown:
            enemy = Enemy()
            self.enemy_group.add(enemy)

    def update(self, player):
        if not len(self.enemy_group):
            self.create_enemy()
        else:
            self.last_live_enemy = pygame.time.get_ticks()
