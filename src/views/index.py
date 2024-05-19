from tkinter import Tk, Frame, Label, Button
from os.path import abspath, dirname

import sys

sys.path.append(dirname(abspath(__file__)))

from configs.screen import WIDTH, HEIGHT, X, Y, BACKGROUND_COLOR
from components.tittle_bar import TitleBar

class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("My Bank")
        #self.overrideredirect(True)  # Remove a barra de título
        self.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")
        self.config(background=BACKGROUND_COLOR)
        self.resizable(False, False)
        
        self.title_bar = TitleBar(self)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()