import pygame
import spacebound.globals as gl


class Health(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = gl.window_width*0.07
        self.y = gl.window_height*0.05
        self.w = gl.window_width*0.2
        self.h = gl.window_height*0.01
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(gl.grey)
        self.rect = self.image.get_rect()
        self.hp = gl.max_hp
        self.max_hp = gl.max_hp

    def progress(self, ratio):
        w = self.w * ratio
        image = pygame.Surface((self.w, self.h))
        image.fill(gl.grey)
        pygame.draw.rect(image, (gl.red), pygame.Rect(0, 0, w, self.h))
        return image

    def update(self):
        self.hp -= 1
        image = self.progress(self.hp / self.max_hp)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
