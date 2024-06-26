

import pygame
pygame.init()
import time


width = 1000
height = 600


running = True
screen = pygame.display.set_mode ((width, height))
background = pygame.image.load('testing_back.png').convert_alpha()
y = 492
x = 100
player_y = y
player_x = x
jumping = False
jump_key_pressed = False
player_image = pygame.image.load("robo_cycle.png")
player_rect = player_image.get_rect(midbottom=(player_x, player_y))
question_block = pygame.image.load("question_block.png")
question_rect = question_block.get_rect(midbottom=(100, 300))
platform_big1 = pygame.image.load("platformbig.png")
big_plat_rect1 = platform_big1.get_rect(midbottom=(276, 385))
floor_image = pygame.image.load('floor.png')
floor_rect = floor_image.get_rect(midbottom=(500, 600))
gravity = 1
jump_height = 20
velocity = jump_height
start_time = pygame.time.get_ticks()
clock = pygame.time.Clock()
player_color = (255, 0, 0)
question_color = (23, 234, 165)
player_rect_outline = pygame.Rect(player_rect.left, player_rect.right, player_rect.width, player_rect.height)
player_rect_outline.inflate_ip(-4, -4)
queston_rect_outline = pygame.Rect(question_rect.left, question_rect.right, question_rect.width, question_rect.height)
queston_rect_outline.inflate_ip(-4, -4)
iscolliding_question = False
iscolliding_bigplat1 = False
coins = 0
isfalling = False



def handle_events():
    global jumping, velocity, iscolliding_bigplat1, iscolliding_question
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                iscolliding_bigplat1 = False
                iscolliding_question = False
                velocity = -jump_height

    return True
    
def update_positions():
    global velocity, jumping, coins, keys, iscolliding_bigplat1, iscolliding_question, isfalling, floor_rect
    
    if player_rect.colliderect(floor_rect) and isfalling:
        player_rect.bottom = floor_rect.top
        velocity = gravity
        jumping = False

    if jumping:
        player_rect.y += velocity
        velocity += gravity

    if velocity > 0:
        isfalling = True

    if velocity < 0:
        isfalling = False
        
#question rect stuff begins

        if player_rect.colliderect(question_rect) and velocity > 0:
            iscolliding_question = True
        
        if iscolliding_question:
            if isfalling:
                player_rect.bottom = question_rect.top
                velocity = 0
                jumping = False

        
        
        if iscolliding_question:
             if not isfalling:
                player_rect.top = question_rect.bottom
                velocity = gravity
                

#big plat stuff begins        
        if player_rect.colliderect(big_plat_rect1):
             iscolliding_bigplat1 = True
        
        if iscolliding_bigplat1:     
            if not isfalling:
                player_rect.top = big_plat_rect1.bottom
                velocity = gravity

        
             
        if iscolliding_bigplat1:
             if isfalling:
                  player_rect.bottom = big_plat_rect1.top
                  velocity = 0
                  jumping = False

        
        
        
        
                        

running = True

while running:
    keys = pygame.key.get_pressed()
    running = handle_events()
    screen.blit(background, (0, 0))
    screen.blit(question_block, question_rect)
    screen.blit(player_image, player_rect)
    screen.blit(floor_image, floor_rect)

    screen.blit(platform_big1, big_plat_rect1)

    update_positions()

    if keys [pygame.K_d] == True:
            player_x += 5

    elif keys [pygame.K_a] == True:
            player_x -= 5

    elif keys [pygame.K_1] == True:
         print("velovity ", velocity)
         print("gravity ", gravity)
         print("player x ", player_x)
         print("player y ", player_rect.bottom)
         print("falling ", isfalling)
         print("floor ", floor_rect.top)

    player_rect.x = player_x
   
    
    if player_x > 1000:
        player_x = 0

    if player_x < 0:
        player_x = 1000

    
            
        

    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


