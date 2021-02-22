import pygame
import random

screen_width = 700
screen_height = 700
#set up the screen and screen size
screen = pygame.display.set_mode((screen_width, screen_height))

#get random location
def getrandomlocation(screenwidth, screenheight):
    randx = random.randint(10, screenwidth - 10)
    randy = random.randint(10, screenheight - 10)
    return randx, randy

#get first apple random location
apple_x, apple_y = getrandomlocation(screen_width, screen_height)

#spawn apple
apple = pygame.draw.circle(screen, (255, 0, 0), (apple_x, apple_y), 15)