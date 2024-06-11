import pygame
import spacebound.globals as gl


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(gl.player_path)
        self.rect = self.image.get_rect()
        x = int(gl.window_width / 2)
        y = gl.window_height - 200
        self.rect.center = [x, y]
