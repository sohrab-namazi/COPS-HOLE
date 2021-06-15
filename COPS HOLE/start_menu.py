
#this file handles the start_menu of thr game with the module "tkinter"

#importing
import pygame
import tkinter as tk
from tkinter import ttk
import sys , time


#creation of window and background
window = tk.Tk()
window.attributes('-fullscreen', True)
bg = tk.PhotoImage(file = "bg.png")
bg_label = tk.Label(window, image=bg)
bg_label.place(x = -8 , y = -8)



#music for start menu
pygame.mixer.init()
bg_music = pygame.mixer.Sound("bg_music.wav")
bg_music.play(-1)

#set the volume of the bg_music on or off
def setting():
    if music["text"] == "MUSIC : ON":
     pygame.mixer.init()
     pygame.mixer.pause()
     music["text"] = "MUSIC : OFF"
    else:
     pygame.mixer.init()
     bg_music = pygame.mixer.Sound("bg_music.wav")
     music["text"] = "MUSIC : ON"
     bg_music.play()
#the button for showing the guiedness of the game
def about():
     import help_about
    
     
#runs the game_loop    
def Play():
 music["text"] = "MUSIC : OFF"
 pygame.mixer.quit()
 import game_part

#registering the name for playing
def Confirm():
    name = names.get()
    file = open("scores.txt" , "a+")
    file.write("{} : 0".format(name))
    file.close()

#ranking of the players og the game
def show_scores():
    
    ##rank determines the nnumber of each player in ranking
    rank = 1

    ##some empty lists ad etc for later uses
    list_keys = []
    scores_dict = {}
    final_text = []

    ##opening file of scores
    file = open("scores.txt" , "r")

    ##geting the whole file as a str and convert it to list that each elements are one specefic line
    file_text = file.read()
    name_scores = file_text.split("\n")

    ##divide each line into the name and the score of the name
    for name_score in name_scores:
        name_score = name_score.split(":")
        try:
         scores_dict[name_score[1]] = name_score[0]
        except:
         pass

    ##collecting all scores and sorting them in decreasing order
    for key in scores_dict.keys():
        key = int(key)
        list_keys.append(key)
        list_keys = sorted(list_keys)
        list_keys.reverse()

    ##producing every line that should be printed in the window of rankings
    for score in list_keys:
        try:
         string = "{}.{} : {}\n".format(rank , scores_dict[" {}".format(str(score))] , score)
        except:
         string = "{}.{} : {}\n".format(rank , scores_dict[" 0{}".format(str(score))] , score)
        rank +=1
        final_text.append(string)
    ##creating the window for showing the ranking    
    win = tk.Tk()
    win.title("SCORES")
    win.configure(background='pink')
    scores_label = tk.Label(win , text = "".join(final_text)  , bg = "pink" , fg = "blue" , font = "COOPBL.ttf").pack()

#this function clears the preview text in Entry after clicking    
def clear_preview(s):
    names.delete(0,30)
  
#GUI

##an Entry for entring the name
names = tk.Entry(bg_label , bg = "pink" , fg = "blue" ,width = 25 , bd = 8 , justify='center')
preview_text = "Please enter your name here"
names.insert(0 , preview_text )
names.place(x = 610 , y = 200)
names.bind("<Button-1>", clear_preview)

##a button for final accepting the name and writing the name in the score_file
confirm = tk.Button(bg_label ,text = "Confirm", bg = "blue" , fg = "red" , width = 10 , height = 1 , command = Confirm)
confirm.place(x = 655 , y = 235)

##a button for entring the game
play = tk.Button( bg_label , text = "PLAY", bg = "red" , fg = "blue" , width = 30 , height = 2, command = Play)
play.place(x = 585 , y = 340)

##a button for settingthe music on and off
music = tk.Button( bg_label , text = "MUSIC : ON", bg = "blue" , fg = "red" , width = 25 , height =2, command = setting)
music.place(x = 602 , y = 381)

##a button for showing the ranking
scores = tk.Button( bg_label , text = "RANKING", bg = "red" , fg = "blue" , width = 20 ,height = 2,   command = show_scores)
scores.place(x = 620 , y = 422)

##guidness button 
about_Help = tk.Button( bg_label , text = "HELP & ABOUT", bg = "blue" , fg = "red" , width = 15 ,height = 2,   command = about)
about_Help.place(x = 635 , y = 463)

##exit button
Quit = tk.Button( bg_label , text = "QUIT", bg = "red" , fg = "blue" , width = 10 , height =2, command = exit)
Quit.place(x = 653 , y = 504)






