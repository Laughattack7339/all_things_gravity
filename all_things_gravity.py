
import pygame
pygame.init()
import time


width = 1000
height = 600


running = True
screen = pygame.display.set_mode ((width, height))
background = pygame.image.load('testing_back.png').convert_alpha()

jumping = False
jump_key_pressed = False
player_image = pygame.image.load("robo_cycle.png")
player_rect = player_image.get_rect(midbottom=(442, 609))
question_block = pygame.image.load("question_block.png")
queston_rect = question_block.get_rect(midbottom=(442, 609))
player_x = 442
player_y = 500
gravity = 1
jump_height = 20
velocity = jump_height
start_time = pygame.time.get_ticks()
clock = pygame.time.Clock()


while running:
    screen.blit(background, (0, 0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                print(player_rect.bottom)
                print(jumping)

    if jumping:
        player_rect.y -= velocity
        velocity -= gravity
        if velocity < -jump_height:
            velocity = jump_height
            jumping = False

   

    

    
        
            
        

    screen.blit(question_block, queston_rect)
    screen.blit(player_image, player_rect)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()


