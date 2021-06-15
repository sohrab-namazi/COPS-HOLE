#this class is used to diagnose the crash of two objects by the lists were created in the game_part

#importing
import pygame  , sys , time 
from class_text import *
from class_money import *

############################

#crash of all the car with police_cars
def intersect(a,b):
   end_a = min(a[1][1] , a[0][1])
   start_a = max(a[1][0] , a[0][0])
   end_b = min(b[1][1] , b[0][1])
   start_b = max(b[1][0] , b[0][0])
   
   if end_a - start_a >= 0:
       if end_b - start_b >= 0:
          import game_part
          game_part.arrest()

########################################

#crash of the car with the money          
def intersect_money(a,b):
   end_a = min(a[1][1] , a[0][1])
   start_a = max(a[1][0] , a[0][0])
   end_b = min(b[1][1] , b[0][1])
   start_b = max(b[1][0] , b[0][0])
   
   if end_a - start_a >= 0:
       if end_b - start_b >= 0:
          import game_part
          game_part.wealth += 1
          game_part.dollar.replace()
#########################################          
         
          

