#this file consistsof a class for writing and showing texts on screen

#importing and initializing
import pygame
pygame.font.init()

###########################

#class
class Text:
    def __init__(self , screen , text ,  font , size ,color ,  position):
        self.screen = screen
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.position = position
        
    ##bliting
    def write(self):
        font_writing = pygame.font.Font(self.font , self.size)
        mold = font_writing.render(self.text , True , self.color)
        self.screen.blit(mold , self.position)

#########################################################################










    

