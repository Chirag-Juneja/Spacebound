
import pygame
from random import randint
from spacebound.sprites.enemy import Enemy
from spacebound.sprites.meteor import Meteor
import spacebound.globals as gl
from spacebound.logger import logger


class FourShip:
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.meteor_group = pygame.sprite.Group()
        self.cooldown = 1000
        self.last_live_enemy = pygame.time.get_ticks()
        self.enemy_count = 4
        self.n_waves = 5
        self.isactive = True
        self.wave_count = 0
        self.formation = "echelon"

    def get_formation_echelon_left(self, live_enemy_count):
        pos = []
        for idx in range(1,live_enemy_count+1):
            w = gl.window_width / (live_enemy_count+1)
            x = idx*(w+1)
            y = idx*gl.window_height*0.1
            pos.append([x,y])
        return pos

    def create_wave(self):
        now = pygame.time.get_ticks()
        if now - self.last_live_enemy > self.cooldown:
            pos = self.get_formation_echelon_left(self.enemy_count)
            for idx in range(self.enemy_count):
                enemy = Enemy(x=pos[idx][0])
                self.enemy_group.add(enemy)
                logger.debug(f"enemy group count {len(self.enemy_group)}")
            self.wave_count += 1
            if self.wave_count > self.n_waves:
                self.isactive = False

    def update(self, player):
        if not len(self.enemy_group):
            self.create_wave()
        else:
            self.last_live_enemy = pygame.time.get_ticks()

        # target = player.x, player.y
        # self.enemy_group.update(target, self.meteor_group)
        live_enemy_count = len(self.enemy_group)
        pos = self.get_formation_echelon_left(live_enemy_count)
        logger.debug(f"positions {pos}")
        for idx,enemy in enumerate(self.enemy_group.sprites()):
            enemy.update(pos[idx],self.meteor_group)

    def enemy_event(self):
        pass

    def meteor_event(self):
        pass
        # meteors = [Meteor() for i in range(randint(0, 2))]
        # self.meteor_group.add(meteors)
