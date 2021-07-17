
import random
import copy
import pygame
class Snake(object):

    def __init__(self, game):
        self.x = .5 * game.game_width
        self.y = .5 * game.game_width
        self.vel_x = 1
        self.vel_y = 0
        self.position = []
        self.position.append([self.x, self.y])
        self.snake_length = len(self.position)
        self.image = pygame.image.load("assets/body.png")
        self.head_image = pygame.image.load("assets/head.png")
        # print(self.position)
    
    
    # control the snakes body with keyboard input
    def move(self, events):
        for event in events:
            # print("pressed")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.vel_x != 1:
                    self.vel_x = -1
                    self.vel_y = 0
                    print('left')
                elif event.key == pygame.K_RIGHT and self.vel_x != -1:
                    self.vel_x = 1
                    self.vel_y = 0
                    print('right')
                elif event.key == pygame.K_UP and self.vel_y != 1:
                    self.vel_x = 0
                    self.vel_y = -1
                    print('up')
                    
                elif event.key == pygame.K_DOWN and self.vel_y != -1:
                    self.vel_x = 0
                    self.vel_y = 1
                    print('down')
        # print(events)
        return events

    # add an additional body square to the snakes tail based on current tails position
    def grow(self, game):
        new_tail = copy.copy(self.position[-1])
        self.position.append(new_tail)
        self.snake_length += 1  

    def get_snake(self):
        for i in range(len(self.position) - 1):
            print(i, self.position[i])

    # update the snakes position based on current direction
    def update(self, game):
        i = self.snake_length - 1
        while i >= 0:
            
            if i == 0:
                if self.vel_x == 1:
                    self.x += 20
                    self.position[i][0] += 20
                elif self.vel_x == -1:
                    self.x -= 20
                    self.position[i][0] -= 20
                elif self.vel_y == 1:
                    self.y += 20
                    self.position[i][1] += 20
                elif self.vel_y == -1:
                    self.y -= 20
                    self.position[i][1] -= 20
            # elif i == len(self.position) - 1:
            #     print(i, self.snake_length)
            elif self.position[i-1][0] > self.position[i][0]:
                self.position[i][0] += 20
            elif self.position[i-1][0] < self.position[i][0]:
                self.position[i][0] -= 20
            elif self.position[i-1][1] > self.position[i][1]:
                self.position[i][1] += 20
            elif self.position[i-1][1] < self.position[i][1]:
                self.position[i][1] -= 20
            
            # show snake body and head images
            if i == 0:
                game.window.blit(self.head_image, (self.position[i][0], self.position[i][1]))
            else:
                game.window.blit(self.image, (self.position[i][0], self.position[i][1]))
            


            # increment place
            i -= 1

        # print("-"*16)
        # self.get_snake()
        # print("-"*16)