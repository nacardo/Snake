import pygame
from game import Game

pygame.init()
pygame.font.init()
FPS = 8
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
FONT = pygame.font.SysFont('arial', 20)

def game_loop():
    clock = pygame.time.Clock()


    game = Game(600, 600)
    snake = game.snake
    food = game.food

    playing = True

    # main game loop
    while playing:
        clock.tick(FPS)
        # clock.get_time()
        events = pygame.event.get()

        # check if 'x' is pressed
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

        # game.window.blit(game.bg, (0,0))
        game.window.fill(BLACK)

        food.show_food(game, food.x, food.y)
        if food.eat_food(game, snake):
            snake.grow(game)
        events = snake.move(events)
        playing = snake.is_dead(game)
        snake.update(game)
        game.show_score(FONT, WHITE)
        
        pygame.display.update()
    game_loop()

game_loop()




