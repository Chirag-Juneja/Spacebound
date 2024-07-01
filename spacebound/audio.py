import pygame
import spacebound.globals as gl


class Audio:
    channels = {
            "background": 0,
            "laser": 1
            }

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load(gl.bg_music)
        pygame.mixer.music.play(-1, 0, 3)
        self._laser = pygame.mixer.Sound(gl.laser_sound)

    def laser(self):
        pygame.mixer.Channel(self.channels["laser"]).play(self._laser)
