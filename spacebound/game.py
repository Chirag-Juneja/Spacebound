import pygame
from .background import Background
from .sprites.player import Player


class Game:

    def __init__(self, resolution, fps):
        pygame.init()
        self.win_h, self.win_w = resolution
        self.create_window()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.bg_path = "./assets/back.png"
        self.player_path = "./assets/player.png"
        self.player = Player(self.player_path, int(self.win_w/2), self.win_h-200)
        self.background = Background(self.bg_path, self.win_h)

    def create_window(self):
        self.screen = pygame.display.set_mode((self.win_h, self.win_w))
        pygame.display.set_caption("SpaceBound")

    def run(self):
        running = True

        player_group = pygame.sprite.Group()

        player_group.add(self.player)

        while running:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.background.update(self.screen)

            player_group.draw(self.screen)

            pygame.display.update()

        pygame.quit()
