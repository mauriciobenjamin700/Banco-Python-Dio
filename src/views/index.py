from tkinter import Tk, Frame, Label, Button
from os.path import abspath, dirname

import sys

sys.path.append(dirname(abspath(__file__)))

from configs.screen import WIDTH, HEIGHT, X, Y, BACKGROUND_COLOR

class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        #self.title("My Bank")
        self.overrideredirect(True)  # Remove a barra de título
        self.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")
        self.config(background=BACKGROUND_COLOR)
        self.resizable(False, False)
        
        self.title_bar = Frame(self, bg='#2e2e2e', relief='raised', bd=0)
        self.title_bar.pack(expand=0, fill='x')
        
        self.title_label = Label(self.title_bar, text="My Bank", bg='#2e2e2e', fg='white', padx=10)
        self.title_label.pack(side='left', padx=10)
        
        self.close_button = Button(self.title_bar, text='✕', bg='#2e2e2e', fg='white', command=self.destroy, bd=0, padx=10)
        self.close_button.pack(side='right', padx=10)

        self.title_bar.bind('<B1-Motion>', self.move_window)
        self.title_bar.bind('<Button-1>', self.get_pos)

        self.main_frame = Frame(self, bg=BACKGROUND_COLOR)
        self.main_frame.pack(expand=1, fill='both')
        
        self.bind('<FocusIn>', self.on_focus_in)
        self.bind('<FocusOut>', self.on_focus_out)


        self.after(10, self.deiconify)  # Mostra a janela após a configuração

    def get_pos(self, event) -> None:
        self._x = event.x
        self._y = event.y

    def move_window(self, event) -> None:
        x = event.x_root - self._x
        y = event.y_root - self._y
        self.geometry(f'+{x}+{y}')
        
    def on_focus_in(self, event) -> None:
        self.after_idle(self.restore_window)

    def on_focus_out(self, event) -> None:
        self.minimize_window()
        
    def restore_window(self) -> None:
        self.overrideredirect(True)
        #self.attributes('-topmost', True)
        #self.after(10, self.attributes, '-topmost', False)

    def minimize_window(self) -> None:
        self.overrideredirect(False)
        #self.attributes('-topmost', True)
        #self.after(10, self.attributes, '-topmost', False)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()