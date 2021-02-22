import sys,random,time
import pygame

pygame.init()

WIN_X = 800
WIN_Y = 600
WIN = pygame.display.set_mode((WIN_X,WIN_Y))
CLOCK = pygame.time.Clock()
pygame.display.set_caption('Project Nibbles')
font=pygame.font.SysFont('comicsans',40)

def writetext(text, x, y, color=(0,0,0), fontsize=24):
    # you have to call this at the start, 
    myfont = pygame.font.SysFont('Arial', fontsize, False, False)
    textsurface = myfont.render(text, True, color)
    WIN.blit(textsurface, (x, y))
 
click = False

#main function
def main_menu():
     while True:
 
        WIN.fill((0,0,0))
        writetext("Nibbles Reboot", 215, 60, (153, 0, 153), 48)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(275, 200, 200, 50)
        
        button_2 = pygame.Rect(275, 300, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(WIN, (255, 0, 0), button_1)
        writetext('Play Game', 300, 205, (200, 200, 0), 30)
        pygame.draw.rect(WIN, (255, 0, 0), button_2)
        writetext('options', 310, 305, (200, 200, 0), 36)
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        CLOCK.tick(60)

def options():
    running = True
    while running:
        WIN.fill((0,0,0))
 
        writetext("Options", 285, 60, (155, 155, 155), 48)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        CLOCK.tick(60)

def game_over(score):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            WIN.fill((0,0,0))
            game_over_message = font.render('You Lost' , True , (255,0,0))
            game_over_score = font.render(f'Your Score was {score}' , True , (255,255,255))

            font_pos_message = game_over_message.get_rect(center=(WIN_X//2, WIN_Y//2))
            font_pos_score = game_over_score.get_rect(center=(WIN_X//2, WIN_Y//2+40))
            WIN.blit(game_over_message , font_pos_message)
            WIN.blit(game_over_score , font_pos_score)
            pygame.display.update()
            time.sleep(3)
            main_menu()


def game():
    snake_pos=[200,70]
    snake_body=[[200,70] , [200-10 , 70] , [200-(2*10),70]]
    fruit_pos = [0,0]
    fruit_spawn = True
    mine_pos = [-10,-10]
    mine_spawn = False
    direction = 'right'
    score=0
    CLOCK = pygame.time.Clock()
    #game loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys= pygame.key.get_pressed()
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and direction != 'down':
                direction = 'up'
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and direction != 'up':
                direction = 'down'
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and direction != 'left':
                direction = 'right'
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and direction != 'right':
                direction = 'left'

        WIN.fill((0,0,0))
        for square in snake_body:
            pygame.draw.rect(WIN ,(255, 255, 0), (square[0],square[1],12,12))
        if direction == 'right':
            snake_pos[0] += 10
        elif direction == 'left':
            snake_pos[0] -= 10
        elif direction == 'up':
            snake_pos[1] -= 10
        elif direction == 'down':
            snake_pos[1] += 10

        snake_body.append(list(snake_pos))

        if fruit_spawn:
            fruit_pos = [random.randrange(40,WIN_X-40),random.randrange(40,WIN_Y-40)]
            fruit_spawn = False

        if mine_spawn:
            mine_pos = [random.randrange(40,WIN_X-40),random.randrange(40,WIN_Y-40)]
            mine_spawn = False

        pygame.draw.rect(WIN ,(138,43,226),(fruit_pos[0],fruit_pos[1],10,10))
        for i in range(3):
            pygame.draw.rect(WIN ,(254,20,20),(mine_pos[0],mine_pos[1],10,10))

        score_font = font.render(f'{score}' , True , (255,255,255))
        font_pos = score_font.get_rect(center=(WIN_X//2-40 , 30))
        WIN.blit(score_font , font_pos)

        if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(fruit_pos[0],fruit_pos[1],10,10)):
            fruit_spawn = True
            score += 100
            if score >= 500:
                mine_spawn = True
            else:
                mine_spawn = False
        else:
            snake_body.pop(0)

        if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(mine_pos[0],mine_pos[1],5,5)):
            game_over(score)
        for square in snake_body[:-1]:
            if pygame.Rect(square[0],square[1],10,10).colliderect(pygame.Rect(snake_pos[0],snake_pos[1],10,10)):
                game_over(score)

        if snake_pos[0]+10 <=0 or snake_pos[0] >= WIN_X:
            game_over(score)
        if snake_pos[1]+10 <=0 or snake_pos[1] >= WIN_Y:
            game_over(score)
        pygame.display.update()

        CLOCK.tick(25)

#caliing the main function
main_menu()
