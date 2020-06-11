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

        # Set up variables
        # time_since_last_turn
        self.TSLT = 0
        # amount/distance to move each step in the X and Y
        self.move_x = random.randint(-2,2)
        self.move_y = random.randint(-2,2)

        #make the image of this sprite
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        # store a  reference to the screen, for positioning and movement
        self.DISPLAYSURF = screen

        # find random starting spot
        self.rect = self.image.get_rect(center = (random.randint(0,self.DISPLAYSURF.get_width()),random.randint(0,self.DISPLAYSURF.get_height())))

    def update(self):
        self.rect.move_ip(self.move_x, self.move_y)
        self.TSLT += 1
        if self.TSLT > random.randint(10,100):
            self.TSLT = 0
            self.move_x = random.randint(-2,2)
            self.move_y = random.randint(-2,2)
        
        if not self.DISPLAYSURF.get_rect().colliderect(self.rect):
            self.rect = self.image.get_rect(center = (random.randint(0,self.DISPLAYSURF.get_width()),random.randint(0,self.DISPLAYSURF.get_height()))) 

        self.DISPLAYSURF.blit(self.image, self.rect)

