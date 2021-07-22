import pygame
from game import Game

pygame.init()
pygame.font.init()
FPS = 10
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
FONT = pygame.font.SysFont('arial', 20)

def game_loop():
    clock = pygame.time.Clock()
    move_delay = 80
    next_move_time = 0
    # increment prints
    p_num = 0

    game = Game(600, 600)
    snake = game.snake
    food = game.food

    playing = True

    # main game loop
    while playing:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()
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


        # keys = pygame.key.get_pressed()
        if current_time > next_move_time:
            events = snake.move(events)
            if events:
                print("changing time")
                next_move_time = current_time + move_delay
        else:
            print(p_num, "- cant move")
            p_num += 1

        playing = snake.is_dead(game)
        snake.update(game)
        game.show_score(FONT, WHITE)
        
        pygame.display.update()
        # print(f"Current: {current_time - next_move_time}")
    game_loop()

game_loop()




