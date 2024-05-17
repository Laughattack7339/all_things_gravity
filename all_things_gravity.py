

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
coins = 0



def handle_events():
    global jumping, velocity
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                velocity = -jump_height

    return True
    
def update_positions():
    global velocity, jumping, coins, keys
    if jumping:
        player_rect.y += velocity
        velocity += gravity
        if player_rect.bottom >= height:
            player_rect.bottom = height

        if player_rect.colliderect(question_rect):
            if velocity > 0:
                jumping = False
                player_rect.y = question_rect.bottom
                velocity = 0

       
        

        
            


        




running = True

while running:
    keys = pygame.key.get_pressed()
    running = handle_events()
    screen.blit(background, (0, 0))
    screen.blit(question_block, question_rect)
    screen.blit(player_image, player_rect)

    update_positions()

    if keys [pygame.K_d] == True:
            player_x += 5

    elif keys [pygame.K_a] == True:
            player_x -= 5
            print("pressed")

    player_rect.x = player_x
            
        

    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


