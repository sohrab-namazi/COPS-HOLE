#this file consists of a class for police_cars 

#importing and police_car dimensions
import pygame , math , sys , time , random
from pygame.locals import *
police_width = 49
police_height = 100

############################################

#class
class Police:
    def __init__(self , speed , kind , screen , x = 0 , y = 0 ):
        self.x = x
        self.y = y
        self.speed = speed
        self. screen = screen
        self.kind = kind
        
    ##creation of the police_car depending on its kind
    def create(self):
        import game_part
        if self.kind == "vertical":
         police = pygame.image.load("police.png")
         police_mold = police.get_rect(center = (self.x,self.y))
         self.screen.blit(police ,police_mold ) 
        elif self.kind == "horizental":
         police = pygame.image.load("police.png")
         police = pygame.transform.rotate(police , 90)
         police_mold = police.get_rect(center = (self.x,self.y))
         self.screen.blit(police , police_mold)

    ##movement of the police_car depending on its kind     
    def move(self):
        if self.kind == "vertical":
             self.y += self.speed
             if self.y >= 600:
                 self.y = 0
                 self.x = random.randrange(10,590)
        if self.kind == "horizental":
             self.x += self.speed
             if self.x >= 600:
                 self.x = 0
                 self.y = random.randrange(10,590)

    ##crashes between polices and disapearing both if happend    
    def crash_polices(self , other):

        ##if both police_cars are horizontal
        if self.kind == "horizental" and other.kind == "horizental":
            if abs(self.y - other.y) < police_height:
                if abs(self.x - other.x) < police_width:
                    self.x = 0
                    other.x = 0
                    self.y = random.randrange(10,590)
                    other.y = random.randrange(10,590)

        ##if the kind of the cars is different
        if (self.kind == "horizental" and other.kind== "vertical") or (self.kind == "vertical" and other.kind== "horizental"):
              if abs(self.x - other.x) < ((police_height+police_width)/2):
                  if abs(self.y - other.y) < ((police_height+police_width)/2):
                      if self.kind == "horizental":
                          self.x = 0
                          self.y = random.randrange(10,590)
                          other.y = 0
                          other.x = random.randrange(10,590)
                      if self.kind == "vertical":
                          self.y = 0
                          self.x = random.randrange(10,590)
                          other.x = 0
                          other.y = random.randrange(10,590)

        ##if both police_cars are vertical
        if self.kind == "vertical" and other.kind == "vertical":
            if abs(self.x - other.x) < police_height:
                if abs(self.y - other.y) <= police_width:
                    self.y = 0
                    other.y = 0
                    self.x = random.randrange(10,590)
                    other.x = random.randrange(10,590)
            
            
                          
                      
             
            
    
        






         


  
    
