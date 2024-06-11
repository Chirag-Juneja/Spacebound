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
        self.player = Player()
        self.background = Background()
        self.meteors = [Meteor() for i in range(3)]

    def create_window(self):
        self.screen = pygame.display.set_mode((gl.window_height, gl.window_width))
        pygame.display.set_caption(gl.window_name)

    def run(self):
        running = True

        player_group = pygame.sprite.Group()

        player_group.add(self.player)
        meteor_group = pygame.sprite.Group()
        meteor_group.add(self.meteors)

        while running:
            self.clock.tick(gl.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.background.update(self.screen)

            player_group.update()
            meteor_group.update()

            player_group.draw(self.screen)
            meteor_group.draw(self.screen)

            pygame.display.update()

        pygame.quit()
