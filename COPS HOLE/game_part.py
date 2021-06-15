#this is the main file of the game that consist the game_loop

#import necessay modules:

import pygame, math, sys , random , intervals_intersect , time
from pygame.locals import *
from class_police  import *
from class_text import *
from class_money import *

###########################################################################################################################################


#define some necessary variables:

##the more the acceleration , the more speedy the car sprints | the more the turn_speed , the faster the car turns
acceleration , turn_speed = 0.8 , 5

##maximum speed that that the car cant exceed it for going straight and back are called "max_forward_speed" and "max_reverse_speed"
max_forward_speed , max_reverse_speed  = 10 , -5

##defining some colors with RGB
white , black , red , green , yellow = (255,255,255) , (0,0,0) , (255 , 0 ,0) , (0,255,0) , (255,255,0)

##defining the limitation of the screen so that the car dosnt go out of it
max_x , max_y = 600 , 600

##the dimensions
car_width = 50
car_height = 50
police_width = 20
police_height = 50
money_width = 83
money_height = 83

##first positoin and quantity of money
dollar_x = random.randrange(50,550)
dollar_y = random.randrange(50,550)
wealth = 0

##defining the navigators of the cars movement
k_up = k_down = k_left = k_right = 0

##initializing the primary speed and direction of the car
speed = direction = 0

##initializing the primary location of the car at the center of the screen | difining an empty list that will be used in another file
position = (max_x/2 , max_y/2) 
pos = []


######################################################################################################################################

#creation & initializing
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((max_x,max_y))
police_x = Police(5 , "horizental" , screen , y = random.randrange(50,550))
police_y = Police(5 , "vertical" , screen , x = random.randrange(50,550))
police_x2 = Police(10 , "horizental" , screen , y = random.randrange(50,550))
police_y2 = Police(10 , "vertical" , screen , x = random.randrange(50,550))
car = pygame.image.load("I.png")
dollar = Money(screen)
clock = pygame.time.Clock()

##loading the sound of horning for the car and polic_car_beeps and officers voice:
horn = pygame.mixer.Sound("horn.wav")
pygame.mixer.music.load("police.wav")
pygame.mixer.music.play(-1)
police_voice = pygame.mixer.Sound("police_voice.wav")
police_voice.play(-1)

#arrest
def arrest():
    global pygame
    
    #showing that the player is busted
    message_fail = Text(screen , "BUSTED!" , "GILLUBCD.TTF" , 100 , red , (130,230))
    
    #showing score
    score = int((3*wealth)+dt)//4
    message_score = Text(screen , "Score : {}".format(score) ,"GILLUBCD.TTF", 50 , green , (200 , 350))
    message_fail.write()
    message_score.write()
    file = open("scores.txt" , "a+")
    file.write("{}\n".format(score))
    pygame.display.update()
    time.sleep(3)
    pygame.mixer.quit()
    pygame.display.quit()

    
    
    

    
    


############################################################################################################################################

#game_loop:

def game_loop():
    t0 = time.time()
    t1 = t0
    global speed , k_up , k_down , k_left , k_right , direction , start_position ,  position , pos , dollar ,dt
    run = True
    ##while true:
    while run:
        ##FPS(frames pes secend) shouldnt exceed by 60:
        clock.tick(60)
        ##searching in events:
        for event in pygame.event.get():
                ##if no key is pressed , dont interrupt. just continue:
                if not hasattr(event, 'key'):
                 continue
                ##hold is a boolean data type , if True , means a key is pressed:
                hold = event.type == KEYDOWN
                ##what to do depend on the key that is pressed:
                if event.key == K_LEFT:
                    k_left = hold * turn_speed
                elif event.key == K_RIGHT:
                    k_right = -(hold * turn_speed)
                elif event.key == K_UP:
                    k_up = hold * acceleration
                elif event.key == K_DOWN:
                    k_down = -(hold * acceleration)
                elif event.key == K_SPACE:
                    horn.play()   
                elif event.key == K_ESCAPE:
                    ##comes out from the loop "while":
                    run = False
                    
        ##creating the background of the game and locating it:
        bg = pygame.image.load("BG.jpg")
        screen.blit( bg, (0,0))
    
        ##the new speed and direction:
        speed += (k_up + k_down)
        direction += (k_right + k_left)
        x , y = position
        
        ##not allowing the car exceedes the limitated speed
        if speed > max_forward_speed:
            speed = max_forward_speed
        if speed < max_reverse_speed:
            speed = max_reverse_speed

        ##just change degree to radian:
        rad = direction * math.pi / 180

        ##the new x and y of the car:
        x += speed*math.sin(rad)
        y += speed*math.cos(rad)

        ##prohabiting the car for giong out of the screen:
        if y < 0:
            y = 0
        elif y > max_y:
            y = max_y
        if x < 0:
            x = 0
        elif x > max_x:
            x = max_x

        ##friction:
        speed -= speed/20  
           
        ##the new position and the list "pos":
        position = (x, y)
        pos = list(position)

        ##rotating the car depending on how much it has turned | creating a rect for the new car:
        rotated_car = pygame.transform.rotate(car, direction)
        mold = rotated_car.get_rect(center = position)

        ##money : showing and calculating
        wealth_written = Text(screen , "Money : {}".format(wealth) ,"GILLUBCD.TTF", 20 , green,(495 , 0))
        wealth_written.write()
        dollar.create()

        ##time : showing and calculating
        t1 = time.time()
        dt = t1 - t0
        t = Text(screen , "Time : {0:.2f}".format(dt) , "GILLUBCD.TTF" , 20 , yellow , (10,0))
        t.write()
        
        ##police : creation and move
        police_x.create()
        police_x.move()
        police_y.create()
        police_y.move()

        ##check the crashes between polices
        Police.crash_polices(police_x,police_y)
        Police.crash_polices(police_x2,police_y2)
        Police.crash_polices(police_x2,police_y)
        Police.crash_polices(police_x,police_y2)
        Police.crash_polices(police_x,police_x2)
        Police.crash_polices(police_y,police_y2)

        ##the intervals of the changes of the position of the car 
        range_car_x = (x-(car_width/2)),(x+(car_width/2))
        range_car_y = (y-(car_height/2)),(y+(car_height/2))

        ##the intervals of the changes of the position of the polices cars and lists of them
        range_police_horizental_x = (police_x.x-(police_width/2)),(police_x.x+(police_width/2))
        range_police_horizental_y = (police_x.y-(police_height/2)),(police_x.y+(police_height/2))
        range_police_vertical_x = (police_y.x-(police_height/2)),(police_y.x+(police_height/2))
        range_police_vertical_y = (police_y.y-(police_width/2)),(police_y.y+(police_width/2))
        range_police_horizental2_x = (police_x2.x- (police_width/2)) , (police_x2.x + (police_width/2))
        range_police_horizental2_y = (police_x2.y - (police_height/2)) , (police_x2.y + (police_height/2))
        range_police_vertical2_x = (police_y2.x-(police_height/2)),(police_y2.x+(police_height/2))
        range_police_vertical2_y = (police_y2.y-(police_width/2)),(police_y2.y+(police_width/2))
        list_horizental_x = [range_car_x,range_police_horizental_x]
        list_horizental_y = [range_car_y,range_police_horizental_y]
        list_vertical_x = [range_car_x,range_police_vertical_x]
        list_vertical_y = [range_car_y,range_police_vertical_y]
        list_horizental2_x = [range_car_x,range_police_horizental2_x]
        list_horizental2_y = [range_car_y,range_police_horizental2_y]
        list_vertical2_x = [range_car_x,range_police_vertical2_x]
        list_vertical2_y = [range_car_y,range_police_vertical2_y]
        
        ##the intervals of the changes of the position of the money and lists of them
        range_money_x = ((dollar.x - (money_width/2)) , (dollar.x + (money_width/2)))
        range_money_y = ((dollar.y - (money_height/2)) , (dollar.y + (money_height/2)))
        list_money_x = [range_car_x,range_money_x]
        list_money_y = [range_car_y,range_money_y]
        
        
        ##adding two faster police_cars fter 20 seconds
        if dt > 20:
            police_x2.create()
            police_x2.move()
            police_y2.create()
            police_y2.move()
        
        ##checking crashes between car and police_cars:
        intervals_intersect.intersect(list_vertical_x,list_vertical_y)
        intervals_intersect.intersect(list_horizental_x,list_horizental_y)
        intervals_intersect.intersect(list_vertical2_x,list_vertical2_y)
        intervals_intersect.intersect(list_horizental2_x,list_horizental2_y)
        intervals_intersect.intersect_money(list_money_x , list_money_y)
        
        ##updating the car and the screen:
        screen.blit(rotated_car, mold)
        pygame.display.flip()

        
    ##exiting       
    sys.exit()

#so the game loop automaticaaly runs after importing game_part:
game_loop()

####################################################################################################################################################
