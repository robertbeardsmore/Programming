import pygame
import random

FPS = 60

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Space")
clock = pygame.time.Clock()     ## For syncing the FPS

width = screen.get_width()
height = screen.get_height()
stars = []
star_count = 1000
for i in range(star_count):
    stars.append([random.randint(0,width), random.randint(0,height), random.randint(2,10)])
## Game loop
running = True
past_time = 0
while running:

    clock.tick(FPS)  
    current_time = pygame.time.get_ticks()  
    for event in pygame.event.get():        
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #3 Draw/render
    screen.fill(BLACK)
    for i in range(star_count):
        pygame.draw.circle(screen, WHITE, (stars[i][0],stars[i][1]), 1)
        change = (20 / (current_time - past_time))
        stars[i][0] -= 0.75 * stars[i][2]
        if stars[i][0] < 0:
            stars[i][0] = width
            stars[i][1] = random.randint(0, height)
            stars[i][2] = random.randint(2, 10)

    

    ## Done after drawing everything to the screen
    pygame.display.flip()   
    past_time = current_time   

pygame.quit()