from tkinter import *
from tkinter.ttk import *
    
    
class Animator():
    def __init__(self):
        self.root = Tk()
        tcl = Tcl()
        print(tcl.call("info", "patchlevel"))

        # giving title to the main window
        self.root.title("First_Program")
        
        # Label is what output will be 
        # show on the window
        label = Label(self.root, text ="Hello World !").pack()
        

    def startAnimating(self):
        # calling mainloop method which is used
        # when your application is ready to run
        # and it tells the code to keep displaying 
        self.root.mainloop()
