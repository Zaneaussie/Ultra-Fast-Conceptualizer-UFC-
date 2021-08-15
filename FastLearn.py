
from tkinter import *
import wikipedia
import nltk
from time import sleep
from tkinter import filedialog
import tkinter.messagebox

learning_data = "This is a test! To run real learning data, upload your learning-package"
learning_data = nltk.word_tokenize(learning_data)

root = Tk()

#Set your desired FPS
FPS = 80

frame_rate = len(learning_data)/FPS
words_per_min = (FPS/1000)
print('Words p/min', words_per_min)

class Window(Frame):

    def __init__(self, master= None):
        Frame.__init__(self, master, bg = "#564C4D")

        self.master = master
        self.init_window()
        self.master.configure(background='#564C4D')
       

    def init_window(self):

        self.master.title('Ultra-Fast-Conceptualizer')
        self.pack(fill=BOTH, expand =1)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)

        menu.add_cascade(label='File', menu=file)
        file.add_command(label='Run Learning Test', command=self.showText)
        file.add_command(label='Exit', command=self.client_exit)
        file.add_command(label='Run Learning Package', command=self.open_file)

        help_menu = Menu(menu)
        menu.add_cascade(label='About', menu=help_menu)
        help_menu.add_command(label='Version 1.0')


    def showText(self):
        
        var = StringVar()
        
        text_data = Label(root,
                          textvariable = var,
                          font="Times 64",
                          bg="##564C4D",
                          width=16,
                          height=8,
                          anchor="center")
        text_data.pack()
        sleep (1)

        for i in (learning_data):
            sleep (frame_rate)
            var.set(i)
            root.update_idletasks()
            
        sleep(2)
        text_data.destroy()


    def client_exit(self):
        
        exit()
           

    def tokenize(self, learning_package):

        self.learning_tokens = nltk.word_tokenize(learning_package)
        self.run_learning_package()


    def open_file(self):
        
        filepath = filedialog.askopenfilename(filetypes=(('text files', 'txt'),))
        print(filepath)

        self.learning_package = open(filepath, 'r')
        self.learning_package = self.learning_package.read()
        self.tokenize(self.learning_package)

    def run_learning_package(self):

        var = StringVar()
        token_data = Label(root,
                          textvariable = var,
                          font="Times 64",
                          bg="##564C4D",
                          width=16,
                          height=8,
                          anchor="center",)

        token_data.pack()
        sleep (1)
        
        for i in (self.learning_tokens):
            sleep (frame_rate)
            var.set(i)
            root.update_idletasks()

        sleep(2)
        token_data.destroy()

        MsgBox = tkinter.messagebox.askquestion ('Choose Action','Run the learning package again?')
        if MsgBox == 'yes':
            self.run_learning_package()

        else:
            pass 


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






