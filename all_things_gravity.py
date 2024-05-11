

import pygame
pygame.init()
import time


width = 1000
height = 600


running = True
screen = pygame.display.set_mode ((width, height))
background = pygame.image.load('testing_back.png').convert_alpha()
player_y = 609
player_x = 442
jumping = False
jump_key_pressed = False
player_image = pygame.image.load("robo_cycle.png")
player_rect = player_image.get_rect(midbottom=(player_x, player_y))
question_block = pygame.image.load("question_block.png")
question_rect = question_block.get_rect(midbottom=(150, 550))

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
player_hitbox = player_rect.inflate(-550, -550)
question_hitbox = question_rect.inflate(-550, -550)

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
    collision = pygame.Rect.colliderect(player_rect, question_rect)
    if collision:
        print(collision)

    

    
        
            
        

    screen.blit(question_block, question_rect)
    screen.blit(player_image, player_rect)

    pygame.draw.rect(screen, player_color, player_hitbox, 4)
    pygame.draw.rect(screen, question_color, question_hitbox, 4)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()


