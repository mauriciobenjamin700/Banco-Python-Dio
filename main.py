from tkinter import (
    Tk,
    Frame,
    Label,
    Button
    )

class myBank(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("My Bank")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.configure(bg="Blue")
        self.main_frame = MainFrame(self)
        self.show_main_frame()
        
    def show_main_frame(self) -> None:
        self.main_frame.pack()
        
    def hide_main_frame(self) -> None:
        self.main_frame.pack_forget()
        
class MainFrame(Frame):
    def __init__(self, master: myBank) -> None:
        super().__init__(master=master)
        self.master = master
        #self.configure(bg="Blue")
        self.create_widgets()
        
        
    def create_widgets(self) -> None:
        self.label = Label(self, text= "Bem Vindo ao My Back APP")
        self.label.pack(pady=10)
        
        self.button1 = Button(self, text="Button 1", command=self.show_screen1())
        self.button1.pack(pady=5)
        
        self.button2 = Button(self, text="Button 2", command=self.show_screen2())
        self.button2.pack(pady=5)
        
        self.button3 = Button(self, text="Button 3", command=self.show_screen3())
        self.button3.pack(pady=5)
        
    def show_screen1(self):
       
        screen1 = Screen(self.master, "Tela 1")
        screen1.pack()

    def show_screen2(self):

        screen2 = Screen(self.master, "Tela 2")
        screen2.pack()

    def show_screen3(self):

        screen3 = Screen(self.master, "Tela 3")
        screen3.pack()
        
class Screen(Frame):
    def __init__(self, master, screen_name) -> None:
        super().__init__(master)
        self.master = master
        self.screen_name = screen_name
        self.create_widgets()

    def create_widgets(self) -> None:
        self.label = Label(self, text=self.screen_name)
        self.label.pack(pady=20)

        self.back_button = Button(self, text="Voltar", command=self.go_back)
        self.back_button.pack(pady=5)

    def go_back(self) -> None:
        self.pack_forget()
        self.master.show_main_frame()
        
if __name__ == "__main__":
    app = myBank()
    app.mainloop()