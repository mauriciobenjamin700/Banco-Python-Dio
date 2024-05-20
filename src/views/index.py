from pickle import INT
from tkinter import Tk, Frame, Label, Button
from os.path import abspath, dirname

import sys

sys.path.append(dirname(abspath(__file__)))

from configs.screen import WIDTH, HEIGHT, X, Y, BACKGROUND_COLOR
from components.tittle_bar import TitleBar

class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("MyBank")

        self.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")
        self.config(background=BACKGROUND_COLOR)
        self.resizable(False, False)
        
        self.welcome = Label(self, text= "Bem vindo ao MyBank Application", font=("Arial",30), background="blue")
        self.welcome.place(relwidth=0.5,relheight=0.1, relx=0.25, rely=0.1)
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()