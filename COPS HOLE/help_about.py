#this flie consists of the guidness and some pointes about the game

#importing
import tkinter as tk

#window for text showing
window = tk.Tk()
window.title("HELP & ABOUT")
window.geometry('800x400')
window.configure(background='yellow')

#the text
Text = "'HELP'\n'Cops Hole' is a 2D exciting car-game that you should control your red car not to be arrested by the police cops.\nit is defined that if the police car almost touches your car , you will be arrested.\nduring the game you should gain money by passing on the money boxes on the screen appear.\nyour score is based on the time you have survived and the amount of money you have stolen.\nit is abvious that money's effect on your score is much more important than the time.\nscore is calculated by this formula:\n'(time + 3*money) / 4'\nin the start menu you can turn the music on or off and also you can check the ranking of players.\nin the start menu you should enter your name so that your score be saved by your name\n.also an exiting button on the start menu is existing.\nand the last point is about car controls, you can use k_left and k_right for turning , k_up for accelerating and k_down for going in reverse mode.\nalso you can press enter for horning as fun!\n\n'ABOUT'\nI am the only creator of this game , this game is not copied from other games at all.\neven if the subject of the game is common , all the regulations and structure of the game is created just by the designer.\nbut all the sounds in this game are come from the site 'freesound' and the code of the game is just written by me.\nHope you enjoy it!\n'SOHRAB NAMAZI'"

#back to menu
def back():
    window.destroy()

#GUI
frame = tk.Frame(window , bg = "yellow")
frame.pack(fill="none", expand=1)
label = tk.Label(frame ,text = Text , bg = "yellow" , fg = "purple" ).pack()
button_exit = tk.Button(frame , text = "back to menu" , command = back , bg = "purple" , fg = "yellow").pack()
