# Flappy Bird
# Imports
import pygame
import random
pygame.init()

WIDTH, HEIGHT = 280, 500
FPS = 20

# Game Setting
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT),pygame.NOFRAME)
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load Images
bg = pygame.image.load("background-day.png")

# Sound FX

# Inital Game Variables
speed = 0
game_started = False
game_over = False
restart = False
score = 0
start_screen = True
pipe_pass = False
pipe_frequency= 5000

# Game Loop
run = True
while run:
    SCREEN.blit(bg, (0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K.ESCAPE:
                    run = False

    pygame.display.update()
    clock.tick(FPS)
