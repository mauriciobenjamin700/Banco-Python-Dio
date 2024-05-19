from tkinter import Frame, Label, Button, Tk

class TitleBar(Frame):
    def __init__(self, master: Tk) -> None:
        super().__init__(master)

        self.configure(bg='#2e2e2e', relief='raised', bd=0)
        self.master = master
        self.master.overrideredirect(True)
        
        
        self.title_label = Label(self, text="My Bank", bg='#2e2e2e', fg='white', padx=10)
        self.title_label.pack(side='left', padx=10)
        
        self.close_button = Button(self, text='✕', bg='#2e2e2e', fg='white', command=self.master.destroy, bd=0, padx=10)
        self.close_button.pack(side='right', padx=10)

        self.bind('<B1-Motion>', self.move_window)
        self.bind('<Button-1>', self.get_pos)

        
        #self.bind('<FocusIn>', self.on_focus_in)
        #self.bind('<FocusOut>', self.on_focus_out)


        #self.after(10, self.deiconify)  # Mostra a janela após a configuração
        
        self.pack(expand=0, fill='x')

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