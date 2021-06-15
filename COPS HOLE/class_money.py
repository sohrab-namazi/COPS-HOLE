#this file consists of a class for creating and replacing money after it is taken

#importing
import pygame , random

########################

#class_definig
class Money:
    def __init__(self , screen , x=random.randrange(50,550) , y=random.randrange(50,550)):
        self.x = x
        self.y = y
        self.screen = screen
    def create(self):
        money = pygame.image.load("$.png")
        money_mold = money.get_rect(center = (self.x , self.y))
        self.screen.blit(money , money_mold)
        
    #this function replaces the money after gaining it
    def replace(self):
        self.x = random.randrange(50,550)
        self.y = random.randrange(50,550)
        self.create()
    
        
        


