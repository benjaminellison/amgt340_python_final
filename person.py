#############
##
##  Class for the person object/sprite
##
#############

#Imports
import pygame, random

class Person(pygame.sprite.Sprite):
    #Constructor
    def __init__(self, screen, color = [125,125,125], width = 10, height = 10):
        #parent class constructor
        pygame.sprite.Sprite.__init__(self)

        #make the image of this sprite
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        # store a  reference to the screen, for positioning and movement
        self.DISPLAYSURF = screen

        self.rect = self.image.get_rect(center = (random.randint(0,self.DISPLAYSURF.get_width()),random.randint(0,self.DISPLAYSURF.get_height())))

    def update():
        pass

    def move(self):
        pass
    

