import pygame
from pygame.locals import *
import random, time
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

import person

pygame.init()

# Setting constants
FPS = 60
FramePerSec = pygame.time.Clock()
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Set up the screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Contagion Simulator")

# Set up Groups
all_sprites = pygame.sprite.Group()
healthy_sprites = pygame.sprite.Group()
sick_sprites = pygame.sprite.Group()

for i in range(30):
    healthy = random.random() > .07
    P = person.Person(DISPLAYSURF, healthy)
    all_sprites.add(P)
    if healthy:
        healthy_sprites.add(P)
    else:
        sick_sprites.add(P)
    

logging.debug('This is a log message.')

# Main loop
while True:
    # parse all events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit(0)

    DISPLAYSURF.fill(WHITE)

    #overlap = pygame.sprite.groupcollide(people, people, False, False)
    
    all_sprites.update()

    pygame.display.update()

    FramePerSec.tick(FPS)


