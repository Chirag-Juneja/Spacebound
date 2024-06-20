import pygame
import spacebound.globals as gl


class Menu:
    def __init__(self):
        self.header_font = pygame.font.Font(gl.font_path, 50)
        self.message_font = pygame.font.Font(gl.font_path, 30)

    def display(self, screen, font, message, x, y):
        message = font.render(message, True, gl.white)
        w = message.get_width()
        _x = int(gl.window_width*x)
        _y = int(gl.window_height*y)
        screen.blit(message, (_x - w//2, _y))

    def main(self, screen):
        self.display(screen, self.header_font ,"SpaceBound", 0.5, 0.2)
        self.display(screen, self.message_font ,"Press Enter to Start", 0.5, 0.5)
