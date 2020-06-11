import pygame, sys
from pygame.locals import *
import random, time

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

# Set up sprites
#P1 = person.Person(DISPLAYSURF, BLUE)


# Set up Groups
people = pygame.sprite.Group()
#people.add(P1)

all_sprites = pygame.sprite.Group()
#all_sprites.add(P1)

for i in range(10):
    P = person.Person(DISPLAYSURF, BLUE)
    people.add(P)
    all_sprites.add(P)


# Main loop
while True:
    # parse all events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    # Move and redraw sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # in case of collision
    ## if pygame.sprite.spritecollideany(P1)

    pygame.display.update()
    FramePerSec.tick(FPS)
