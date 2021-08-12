from tkinter import *
import wikipedia
import nltk
from time import sleep

learning_data = "Tomorrow is Friday woohoo, let's dance"
learning_data = nltk.word_tokenize(learning_data)
print (len(learning_data))

#Set your desired FPS
FPS = 60


class Window(Frame):

    def __init__(self, master= None):
        Frame.__init__(self, master, bg = "#564C4D")

        self.master = master
        self.init_window()
        self.master.configure(background='#564C4D')
       

    def init_window(self):

        self.master.title('Ultra-Conceptualizer')
        self.pack(fill=BOTH, expand =1)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)

        menu.add_cascade(label='File', menu=file)
        file.add_command(label='Run', command=self.showText)
        file.add_command(label='Exit', command=self.client_exit)
        file.add_command(label='Upload Data', command=self.client_exit)

        help_menu = Menu(menu)
        menu.add_cascade(label='About', menu=help_menu)
        help_menu.add_command(label='Version 1.0')


    def showText(self):
        
        var = StringVar()
        
        text_data = Label(root,
                          textvariable = var,
                          font="Times 64",
                          bg="#564C4D",
                          width=16,
                          height=8,
                          anchor="center")
        text_data.pack()
        sleep (1)

        for i in (learning_data):
            sleep (frame_rate)
            var.set(i)
            root.update_idletasks()
            


    def client_exit(self):
        exit()


root = Tk()


w = 1200 # width of the window
h = 600 # height of the window

# get screen width and height
ws = root.winfo_screenwidth() 
hs = root.winfo_screenheight()

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# Set Window size
root.geometry('%dx%d+%d+%d'% (w, h, x, y))

app = Window(root)
root.mainloop()



