#importing libaries
import pygame
import time,random

speed = 15
#defining window size
window_x = 720
window_y = 480

#defining color
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

#initialising game
pygame.init()
pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock() # fps controller

# defining snake position
snake_pos = [100,50]
snake_body = [ [100,50],
              [90,50],
              [80,50],
              [70,50]
              ]
#fruit postion
fruit_pos = [random.randrange(1, (window_x//10))*10,
             random.randrange(1, (window_y//10))*10]
fruit_spawn = True
#setting snake direction
direction = "RIGHT"
change_to = direction
#score function
score = 0
def show_score(choice,color,font,size):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score: '+ str(score),True,color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
#game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman',50)
    game_over_surface = my_font.render("Your Score is:" + str(score),True,red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    #game sleep time
    time.sleep(2) # game sleep in 2 sec
    pygame.quit()
    quit()
    
#main function
while True:
    #handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    #if two keys are pressed simultaneouslu
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    #moving snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    
    #snake growing mechanism
    snake_body.insert(0,list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and  snake_pos[1] == fruit_pos[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (window_x//10))*10,
                          random.randrange(1, (window_y//10))*10]
    fruit_spawn = True
    game_window.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(game_window,green,pygame.Rect(
            pos[0],pos[1],10,10))
    pygame.draw.rect(game_window,white,pygame.Rect(
        fruit_pos[0],fruit_pos[1],10,10))
    #game over conditons
    if snake_pos[0] < 0 or snake_pos[0] > window_x - 10 :
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > window_y - 10 :
        game_over()
    # touching snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    #display score continously
    show_score(1,white,'times new roman',20)
    #refresh game screen
    pygame.display.update()
    
    #frame pre sec / refresh rate
    fps.tick(speed)
    