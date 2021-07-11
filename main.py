import pygame
from game import Game

FPS = 3
BLACK = [0, 0, 0]


pygame.init()
clock = pygame.time.Clock()


game = Game(600, 600)
snake = game.snake
food = game.food

playing = True

# main game loop
while playing:
    clock.tick(FPS)
    events = pygame.event.get()

    # check if 'x' is pressed
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    # game.window.blit(game.bg, (0,0))
    game.window.fill(BLACK)

    food.show_food(game, food.x, food.y)
    food.eat_food(game, snake)
    events = snake.move(events)
    snake.update(game)
    pygame.display.update()




