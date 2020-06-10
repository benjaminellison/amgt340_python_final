#############
##
##  Class for the person object/sprite
##
#############

#Imports
import pygame

class Person(pygame.sprite.Sprite):
    #Constructor
    def __init__(self, color, width = 10, height = 10):
        #parent class constructor
        pygame.sprite.Sprite.__init__(self)

        #make the image of this sprite
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def update():
        pass

    def move(self):
        pass
    

