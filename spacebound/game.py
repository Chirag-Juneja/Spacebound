import pygame
from pygame import mixer
from random import randint
import spacebound.globals as gl
from .background import Background
from .sprites.player import Player
from .sprites.meteor import Meteor


class Game:

    def __init__(self):
        pygame.init()
        mixer.init()
        self.create_window()
        self.clock = pygame.time.Clock()
        self.event_counter = 1
        self.load_sprites()
        self.play_music()

    def play_music(self):
        mixer.music.load(gl.bg_music)
        mixer.music.play(-1, 0, 3)

    def create_window(self):
        self.screen = pygame.display.set_mode((gl.window_height, gl.window_width))
        pygame.display.set_caption(gl.window_name)

    def load_sprites(self):
        self.player = Player()
        self.background = Background()

        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        self.meteor_group = pygame.sprite.Group()
        self.add_meteors()
        self.create_events()

    def create_events(self):
        self.METEOR_EVENT = pygame.USEREVENT + self.event_counter
        pygame.time.set_timer(self.METEOR_EVENT, 1000)
        self.event_counter += 1

    def update(self):
        self.player_group.update()
        self.meteor_group.update()

    def draw(self):
        self.background.draw(self.screen)
        self.player_group.draw(self.screen)
        self.meteor_group.draw(self.screen)

    def add_meteors(self):
        meteors = [Meteor() for i in range(randint(0, 3))]
        self.meteor_group.add(meteors)

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.player.move(-gl.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.player.move(gl.speed, 0)
        if keys[pygame.K_UP]:
            self.player.move(0, -gl.speed)
        if keys[pygame.K_DOWN]:
            self.player.move(0, gl.speed)

    def collision(self):
        running = True
        if pygame.sprite.groupcollide(self.player_group, self.meteor_group, False, False):
            running = False
        return running

    def run(self):
        running = True
        while running:
            self.clock.tick(gl.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == self.METEOR_EVENT:
                    self.add_meteors()
            keys = pygame.key.get_pressed()
            self.handle_input(keys)
            running = self.collision()
            self.update()
            self.draw()

            pygame.display.update()

        pygame.quit()
