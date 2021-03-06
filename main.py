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

# add 50 sprites to the screen
for i in range(50):
    # there's a 93% chance a sprite is healthy
    healthy = random.random() > .07
    P = person.Person(DISPLAYSURF, healthy)
    all_sprites.add(P)
    if healthy:
        healthy_sprites.add(P)
    else:
        sick_sprites.add(P)
    

#logging.debug('This is a log message.')

# Main loop
while True:
    # parse all events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit(0)

    # fill the background with solid white
    DISPLAYSURF.fill(WHITE)

    # find and iterate over the collisions between sick sprites and healthy ones
    # groupcollide returns a dictionary where  all the sick ones are keys and the values are a list of healthy collisions
    overlap = pygame.sprite.groupcollide(sick_sprites, healthy_sprites, False, False)
    for sicko, exposedPeeps in overlap.items():
        # every healthy sprite that overlaps a sick one.
        for exposed in exposedPeeps:
            # toggle the newly infected sprite attribute and
            # shuffle it between groups
            exposed.healthy = False
            sick_sprites.add(exposed)
            healthy_sprites.remove(exposed)
            

    # call the update routine for all the sprites
    all_sprites.update()

    # paint the changes to the screen
    pygame.display.update()

    # waits a set amount of time
    FramePerSec.tick(FPS)


