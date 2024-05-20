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

        self.master.bind('<Map>', self.on_map)  # When the window is mapped (shown)
        self.master.bind('<Unmap>', self.on_unmap)  # When the window is unmapped (hidden)

        self.pack(expand=0, fill='x')

    def get_pos(self, event) -> None:
        self._x = event.x
        self._y = event.y

    def move_window(self, event) -> None:
        x = event.x_root - self._x
        y = event.y_root - self._y
        self.master.geometry(f'+{x}+{y}')
        
    def on_map(self, event) -> None:
        self.master.overrideredirect(True)
        self.master.attributes('-topmost', True)
        self.master.after(10, lambda: self.master.attributes('-topmost', False))

    def on_unmap(self, event) -> None:
        self.master.overrideredirect(False)

if __name__ == "__main__":
    root = Tk()
    root.geometry("400x300+100+100")
    root.config(bg="blue")
    TitleBar(root)
    root.mainloop()
