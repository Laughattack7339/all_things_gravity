import pygame
pygame.init()


width = 1000
height = 600


screen = pygame.display.set_mode((width, height))

background = pygame.image.load('testing_back.png').convert_alpha()
player_image = pygame.image.load("robo_cycle.png")
platform_big1 = pygame.image.load("platformbig.png")
floor_image = pygame.image.load('floor.png')
small_mover1 = pygame.image.load('little_mover.png')
small_plat = pygame.image.load('smol_platl.png')
space = pygame.image.load('space.png')

frame_width = 36
frame_height = 64
num_frames = 12




player_rect = player_image.get_rect(midbottom=(100, 492))
big_plat_rect1 = platform_big1.get_rect(midbottom=(276, 385))
floor_rect = floor_image.get_rect(midbottom=(500, 600))
small_mover1_rect = small_mover1.get_rect(midbottom=(700, 250))
small_plat_rect = small_plat.get_rect(midbottom=(300, 200))


gravity = 1
jump_height = 20

velocity = jump_height
clock = pygame.time.Clock()

jumping = False
isfalling = True
coins = 0
show_hitboxes = False
moving_right = True
in_space = False

animation_index = 0
animation_speed = 0.1
animation_timer = 0

def handle_events():
    global jumping, velocity, show_hitboxes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                velocity = -jump_height
            elif event.key == pygame.K_h:
                show_hitboxes = not show_hitboxes
    return True

def update_positions():
    global velocity, jumping, isfalling, gravity, in_space
    in_space = False
    if jumping:
        player_rect.y += velocity
        velocity += gravity

   
    if player_rect.colliderect(floor_rect):
        player_rect.bottom = floor_rect.top
        velocity = gravity
        jumping = False
        isfalling = False

    
   
   
    if player_rect.colliderect(big_plat_rect1):
        if velocity > 0:  
            player_rect.bottom = big_plat_rect1.top
            velocity = 0
            jumping = False
        
         
        else: 
            player_rect.top = big_plat_rect1.bottom
            velocity = gravity

    
    if player_rect.colliderect(big_plat_rect1):
        if player_rect.left == big_plat_rect1.right:
            player_rect.left = big_plat_rect1.right
    
    
    if player_rect.colliderect(small_mover1_rect):
        if velocity > 0:
            player_rect.bottom = small_mover1_rect.top
            velocity = 0
            jumping = False

        else: 
            player_rect.top = small_mover1_rect.bottom
            velocity = gravity

    if player_rect.colliderect(small_plat_rect):
        if velocity > 0:
            player_rect.bottom = small_plat_rect.top
            velocity = 0
            jumping = False

        else:
            player_rect.top = small_plat_rect.bottom        
            velocity = gravity


    if not player_rect.colliderect(floor_rect) and not player_rect.colliderect(big_plat_rect1):
        isfalling = True
    else:
        isfalling = False

    if isfalling and not jumping:
        velocity += gravity
        player_rect.y += velocity

    


    

def move_platform():
    global moving_right
    if moving_right:
        small_mover1_rect.x += 1
        if small_mover1_rect.x >= 750:
            moving_right = False
    else:
        small_mover1_rect.x -= 1
        if small_mover1_rect.x <= 550:
            moving_right = True

    







running = True

while running:
    running = handle_events()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_d]:
        player_rect.x += 5
    if keys[pygame.K_a]:
        player_rect.x -= 5
    if keys[pygame.K_1]:
        print(f"velocity: {velocity}, gravity: {gravity}, player x: {player_rect.x}, player y: {player_rect.y}, falling: {isfalling}, floor: {floor_rect.top}")
        print(small_mover1_rect.x)
    update_positions()
    move_platform()
    

    
    
    if player_rect.right > width:
        player_rect.left = 0
        
    if player_rect.left < 0:
        player_rect.right = 1001

    
    screen.blit(background, (0, 0))
    screen.blit(player_image, player_rect)
    screen.blit(floor_image, floor_rect)
    screen.blit(platform_big1, big_plat_rect1)
    screen.blit(small_mover1, small_mover1_rect)
    screen.blit(small_plat, small_plat_rect)
    
    if show_hitboxes:
        pygame.draw.rect(screen, (255, 0, 0), player_rect, 2)         
        pygame.draw.rect(screen, (0, 0, 255), big_plat_rect1, 2)    
        pygame.draw.rect(screen, (255, 255, 0), floor_rect, 2)
    
    if player_rect.y <= 0:
        in_space = True

    if in_space:
        player_rect.y = 599
        screen.blit(space, (0, 0))
        screen.blit(player_image, player_rect)
    

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
