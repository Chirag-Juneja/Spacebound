# import pygame
# import math
# from spacebound.game import Game

# pygame.init()
# window_h = 1024
# window_w = 1024
# fps = 60

# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((window_h, window_w))
# pygame.display.set_caption("SpaceBound")

# bg = pygame.image.load("./assets/back.png").convert()
# bg_h = bg.get_height()
# scroll =window_h-bg_h
# running = True
# while running:

#     clock.tick(fps)


#     screen.blit(bg,(0,scroll))
#     if scroll>0:
#         screen.blit(bg,(0,scroll-bg_h))
#     if scroll>window_h:
#         scroll=window_h-bg_h

#     scroll+=5

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.display.update()

# pygame.quit()

from spacebound.game import Game

game = Game((1024,1024),60)
game.run()
