import pygame
import spacebound.globals as gl
from .background import Background
from .sprites.player import Player
from .sprites.meteor import Meteor


class Game:

    def __init__(self):
        pygame.init()
        self.create_window()
        self.clock = pygame.time.Clock()
        self.load_sprites()

    def create_window(self):
        self.screen = pygame.display.set_mode((gl.window_height, gl.window_width))
        pygame.display.set_caption(gl.window_name)

    def load_sprites(self):
        self.player = Player()
        self.background = Background()
        self.meteors = [Meteor() for i in range(3)]

        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        self.meteor_group = pygame.sprite.Group()
        self.meteor_group.add(self.meteors)

    def update(self):
        self.player_group.update()
        self.meteor_group.update()

    def draw(self):
        self.background.draw(self.screen)
        self.player_group.draw(self.screen)
        self.meteor_group.draw(self.screen)

    def run(self):
        running = True
        while running:
            self.clock.tick(gl.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()
            self.draw()

            pygame.display.update()

        pygame.quit()
