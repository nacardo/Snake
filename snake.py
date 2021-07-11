import pygame

class Snake(object):
    def __init__(self, game):
        self.x = .5 * game.game_width
        self.y = .5 * game.game_width
        self.vel_x = 1
        self.vel_y = 0
        self.position = []
        # self.position.extend([[self.x, self.y], [self.x - 20, self.y]])
        self.position.extend(self.x, self.y)
        self.image = pygame.image.load("assets/body.png")
        print(self.position)
    
    
    # control the snakes body with keyboard input
    def move(self, events):
        for event in events:
            # print("pressed")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.vel_x != 1:
                    self.vel_x = -1
                    self.vel_y = 0
                    # print('left')
                elif event.key == pygame.K_RIGHT and self.vel_x != -1:
                    self.vel_x = 1
                    self.vel_y = 0
                    # print('right')
                elif event.key == pygame.K_UP and self.vel_y != 1:
                    self.vel_x = 0
                    self.vel_y = -1
                    # print('up')
                    
                elif event.key == pygame.K_DOWN and self.vel_y != -1:
                    self.vel_x = 0
                    self.vel_y = 1
                    # print('down')
        # print(events)
        return events

    # add an addition body square to the snakes tail based on current tails position
    def grow(self, game):
        self.position.append(self.position[-1])

    # update the snakes position based on current direction
    def update(self, game):
        if self.vel_x == 1:
            self.x += 20
        elif self.vel_x == -1:
            self.x -= 20
        elif self.vel_y == 1:
            self.y += 20
        elif self.vel_y == -1:
            self.y -= 20

        game.window.blit(self.image, (self.x, self.y))
        # print(f"vel_x: {self.vel_x}, vel_y: {self.vel_y}")