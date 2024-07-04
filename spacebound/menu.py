import pygame
import spacebound.globals as gl


class Menu:
    def __init__(self):
        self.header_font = pygame.font.Font(gl.font_path, 50)
        self.message_font = pygame.font.Font(gl.font_path, 30)

    def display(self, screen, font, message, x, y):
        message = font.render(message, True, gl.white)
        w = message.get_width()
        _x = int(gl.window_width * x)
        _y = int(gl.window_height * y)
        screen.blit(message, (_x - w // 2, _y))

    def main(self, screen):
        running = True
        mode = "menu"
        self.display(screen, self.header_font, "SpaceBound", 0.5, 0.2)
        self.display(screen, self.message_font, "Press Enter to Start", 0.5, 0.5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "play"
        return running, mode

    def retry(self, screen, score):
        running = True
        mode = "retry"
        self.display(screen, self.header_font, f"Score: {score}", 0.5, 0.2)
        self.display(screen, self.message_font, "Press Enter to Retry", 0.5, 0.5)
        self.display(screen, self.message_font, "Press Esc to Exit", 0.5, 0.7)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "play"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        return running, mode

    def end(self, screen, score):
        running = True
        mode = "end"
        self.display(screen, self.header_font, f"Score: {score}", 0.5, 0.2)
        self.display(screen, self.header_font, "Congratulations", 0.5, 0.5)
        self.display(screen, self.message_font, "Press Enter to Play again", 0.5, 0.7)
        self.display(screen, self.message_font, "Press Esc to Exit", 0.5, 0.8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "play"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        return running, mode
