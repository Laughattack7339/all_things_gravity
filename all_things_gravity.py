
import pygame
pygame.init()


width = 1000
height = 600


running = True
screen = pygame.display.set_mode ((width, height))
background = pygame.image.load('testing_back.png').convert_alpha()

jumping = False
jump_key_pressed = False

player_x = 300
player_y = 442
player = pygame.Rect(player_x, player_y, 50, 50)
gravity = 1
jump_height = 20
velocity = jump_height
start_time = pygame.time.get_ticks()


while running:
    
    
    screen.blit(background, (0, 0))
    rect= pygame.draw.rect(screen, (48, 3, 252), player)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        jumping = True

    if jumping:
        player_y -= velocity
        velocity -= gravity
        if velocity < -jump_height:
            jumping = False
            velocity = jump_height
        rect

    else:
            
        

    

    player.topleft = (player_x, player_y)
    pygame.display.flip()

pygame.quit()


