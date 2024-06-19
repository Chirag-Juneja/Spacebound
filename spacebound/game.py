import pygame
from pygame import mixer
from random import randint
import spacebound.globals as gl
from .background import Background
from .sprites.player import Player
from .sprites.meteor import Meteor
from .sprites.laser import Laser
from .sprites.enemy import Enemy


class Game:

    def __init__(self):
        pygame.init()
        mixer.init()
        self.create_window()
        self.font = pygame.font.Font(gl.font_path, 20)
        self.clock = pygame.time.Clock()
        self.event_counter = 1
        self.load_sprites()
        self.play_music()
        self.score = 0

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

        self.enemy_group = pygame.sprite.Group()

        self.player_laser_group = pygame.sprite.Group()

        self.enemy_laser_group = pygame.sprite.Group()

        self.create_events()

    def create_events(self):
        self.METEOR_EVENT = pygame.USEREVENT + self.event_counter
        pygame.time.set_timer(self.METEOR_EVENT, 1000)
        self.event_counter += 1
        self.SCORE_EVENT = pygame.USEREVENT + self.event_counter
        pygame.time.set_timer(self.SCORE_EVENT, 1000)
        self.event_counter += 1
        self.ENEMY_EVENT = pygame.USEREVENT + self.event_counter
        pygame.time.set_timer(self.ENEMY_EVENT, 500)
        self.event_counter += 1

    def create_enemy(self):
        enemy = Enemy()
        self.enemy_group.add(enemy)

    def update(self):
        self.player_group.update()
        self.meteor_group.update()
        self.player_laser_group.update()
        self.enemy_laser_group.update()
        if not len(self.enemy_group):
            self.create_enemy()
        target = self.player.x, self.player.y
        self.enemy_group.update(target)

    def draw(self):
        self.background.draw(self.screen)
        self.meteor_group.draw(self.screen)
        self.player_laser_group.draw(self.screen)
        self.enemy_laser_group.draw(self.screen)
        self.player_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.draw_score()

    def add_meteors(self):
        meteors = [Meteor() for i in range(randint(0, 3))]
        self.meteor_group.add(meteors)

    def fire(self):
        laser = self.player.fire()
        if laser:
            self.player_laser_group.add(laser)

    def handle_input(self, keys):
        if not len(self.player_group):
            return
        if keys[pygame.K_LEFT]:
            self.player.move(-gl.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.player.move(gl.speed, 0)
        if keys[pygame.K_UP]:
            self.player.move(0, -gl.speed)
        if keys[pygame.K_DOWN]:
            self.player.move(0, gl.speed)
        if keys[pygame.K_SPACE]:
            self.fire()

    def collision(self):
        player_collision = pygame.sprite.groupcollide(
            self.player_group, self.meteor_group, False, False
        )
        for player in player_collision:
            player.destroy = True
        enemy_laser_collisions = pygame.sprite.groupcollide(
            self.enemy_laser_group, self.meteor_group, False, False
        )
        for laser in enemy_laser_collisions:
            laser.hit = True
        player_laser_collisions = pygame.sprite.groupcollide(
            self.player_laser_group, self.meteor_group, False, False
        )
        for laser in player_laser_collisions:
            laser.hit = True
        player_collision = pygame.sprite.groupcollide(
            self.player_group, self.enemy_laser_group, False, False
        )
        for player in player_collision:
            player.destroy = True
        enemy_collision = pygame.sprite.groupcollide(
            self.enemy_group, self.player_laser_group, False, False
        )
        for enemy in enemy_collision:
            enemy.destroy = True

    def enemy_ai(self):
        for enemy in self.enemy_group.sprites():
            laser = enemy.fire()
            if laser:
                self.enemy_laser_group.add(laser)

    def draw_text(self, text, color, x, y):
        img = self.font.render(text, True, color)
        w = img.get_width()
        self.screen.blit(img, (x - w // 2, y))

    def update_score(self):
        self.score += 1

    def draw_score(self):
        x = int(gl.window_width / 2)
        y = int(gl.window_height * 0.05)
        self.draw_text("Score: " + str(self.score), gl.white, x, y)

    def run(self):
        running = True
        while running:
            self.clock.tick(gl.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == self.METEOR_EVENT:
                    self.add_meteors()
                if event.type == self.SCORE_EVENT:
                    self.update_score()
                if event.type == self.ENEMY_EVENT:
                    self.enemy_ai()

            keys = pygame.key.get_pressed()

            self.handle_input(keys)
            self.collision()
            self.update()
            self.draw()

            pygame.display.update()

        pygame.quit()
