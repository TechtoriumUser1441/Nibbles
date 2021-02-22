import pygame
import random

#initialize pygame
pygame.init()
pygame.font.init()



#define variables
screentype = 1 #1 = start screen, 2 = game screen, 3 =  end screen

screen_width = 700
screen_height = 700

worm_x = [350,330,310,290]
worm_y = [350,350,350,350]

wormblocksize = 20;

up = False;
down = False;
left = False;
right = False;


#set up the screen and screen size
screen = pygame.display.set_mode((screen_width, screen_height))

#write some text
def writetext(text, x, y, color=(0,0,0), fontsize=24):
    # you have to call this at the start, 
    myfont = pygame.font.SysFont('Arial', fontsize, False, False)
    textsurface = myfont.render(text, True, color)
    screen.blit(textsurface, (x, y))


#draw worm
def drawworm(wrm_x, wrm_y):
    for i in range(len(worm_x)):
        #draw worm shadow
        pygame.draw.rect(WIN ,(255, 255, 0), (square[0],square[1],10,10))

    for i in range(len(worm_x)):
        #draw worm body
        pygame.draw.circle(screen, (153, 0, 153), (worm_x[i], worm_y[i]), 15)

#get random location
def getrandomlocation(screenwidth, screenheight):
    randx = random.randint(10, screenwidth - 10)
    randy = random.randint(10, screenheight - 10)

    return randx, randy


#get first apple random location
apple_x, apple_y = getrandomlocation(screen_width, screen_height)

#initialize the main game loop
running = True
while running:

    
    #start screen
    if screentype == 1:
        screen.fill((0, 0, 0))
        writetext("Nibbles Reboot", 200, 200, (153, 0, 153), 48)
        writetext("press enter to play", 250, 250, (255, 255, 255))
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        screentype = 2

    #game screen
    if screentype == 2:
        #speed of game
        pygame.time.delay(70)

        #fill background
        screen.fill((92, 230, 131))

        #go through events and see if close button was click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if(right):
                        pass
                    else:
                        left = True
                        right, up, down = False, False, False
                elif event.key == pygame.K_RIGHT:
                    if(left):
                        pass
                    else:
                        right = True
                        left, up, down = False, False, False
                elif event.key == pygame.K_UP:
                    if(down):
                        pass
                    else:
                        up = True
                        right, left, down = False, False, False
                elif event.key == pygame.K_DOWN:
                    if(up):
                        pass
                    else:
                        down = True
                        right, left, up = False, False, False     
    
        #draw a red circle
        apple = pygame.draw.circle(screen, (255, 0, 0), (apple_x, apple_y), 15)
        drawworm(worm_x, worm_y)

        #move worm in direction
        if(right):
            worm_x.insert(0, worm_x[0] + wormblocksize)
            worm_x.pop()
            worm_y.insert(0, worm_y[0])
            worm_y.pop()

        if(left):
            worm_x.insert(0, worm_x[0] - wormblocksize)
            worm_x.pop()
            worm_y.insert(0, worm_y[0])
            worm_y.pop()

        if(down):
            worm_x.insert(0, worm_x[0] )
            worm_x.pop()
            worm_y.insert(0, worm_y[0] + wormblocksize)
            worm_y.pop()

        if(up):
            worm_x.insert(0, worm_x[0])
            worm_x.pop()
            worm_y.insert(0, worm_y[0] - wormblocksize)
            worm_y.pop()


        #boundaries
        if (worm_x[0] < 0) or (worm_x[0] > screen_width) or (worm_y[0] < 0) or (worm_y[0] > screen_height):
            screentype = 3

    #end screen
    if screentype == 3:
        screen.fill((0, 0, 0))
        writetext("GAME OVER = YOU SUCK!!!", 100, 200, (255, 0, 0), 48)
        writetext("press R to play again", 250, 250, (255, 255, 255))
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        screentype = 2
                        worm_x = [350,330,310,290]
                        worm_y = [350,350,350,350]


    #update the game screen with latest
    pygame.display.update()

pygame.quit()