import pygame
from food import Food
from snake import Snake


class Game:

    def __init__(self, game_width, game_height):
        pygame.display.set_caption("Snake")
        self.game_width = game_width
        self.game_height = game_height
        self.food = Food()
        self.snake = Snake(self)

        self.window = pygame.display.set_mode((self.game_width, self.game_height))
        self.score = 0
        # self.bg = pygame.transform.scale(pygame.image.load("assets/background.png"),(self.game_width, self.game_height))
        # self.bg = self.window.fill(BLACK)

    def show_score(self, font, color):
        self.window.blit(font.render(f"Score: {str(self.score)}", 1, color), (10, 20))
