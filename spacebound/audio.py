import pygame
import spacebound.globals as gl


class Audio:
    channels = {"background": 0, "laser": 1, "explosion": 2}

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load(gl.bg_music)
        pygame.mixer.music.play(-1, 0, 3)
        self._laser = pygame.mixer.Sound(gl.laser_sound)
        self._explosion_player = pygame.mixer.Sound(gl.explosion_sound_player)
        self._explosion_enemy = pygame.mixer.Sound(gl.explosion_sound_enemy)

    def laser(self):
        pygame.mixer.Channel(self.channels["laser"]).play(self._laser)

    def explosion_enemy(self):
        pygame.mixer.Channel(self.channels["explosion"]).play(self._explosion_enemy)

    def explosion_player(self):
        pygame.mixer.Channel(self.channels["explosion"]).play(self._explosion_player)
