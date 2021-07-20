import random
import pygame
# from game import Game

class Food(object):
    def __init__(self):
        self.x = 300
        self.y = 100
        self.food_image = pygame.image.load("assets/food.png")

    def new_food(self, game, snake):
        self.x = random.randint(0, game.game_width // 20) * 20
        self.y = random.randint(0, game.game_height // 30) * 20
        for pos in game.snake.position:
            if [self.x, self.y] == pos:
                self.new_food(game, snake)
                print("food in snake")


    
    def show_food(self, game, x, y):
        game.window.blit(self.food_image, (x,y))
        pygame.display.update()

    def eat_food(self, game, snake):
        if game.snake.x == self.x and game.snake.y == self.y:
            self.new_food(game, snake)
            game.score += 1
            return True