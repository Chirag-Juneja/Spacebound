import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, path, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
