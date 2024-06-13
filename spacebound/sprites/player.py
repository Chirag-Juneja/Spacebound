import pygame
import spacebound.globals as gl


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(gl.player_path)
        self.rect = self.image.get_rect()
        self.x = int(gl.window_width / 2)
        self.y = gl.window_height - int(gl.window_height*0.1)
        self.rect.center = [self.x, self.y]

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

    def update(self):
        self.rect.center = [self.x, self.y]
