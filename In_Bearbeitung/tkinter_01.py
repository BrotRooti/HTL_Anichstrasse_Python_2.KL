from tkinter import *
import time
from random import randint

class Reaction(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.info_label = Label(self, text="Dies ist ein einfacher Reaktionstest",font=("Arial", 25))
        self.main_button = Button(self, text="Start",
                             command=self.init_timer,bg="red",font=("Arial", 20))
        self.info_label.pack()
        self.main_button.pack()
        self.pack()

    def init_timer(self):
        self.info_label["text"] = "Warte auf das Signal"
        self.info_label["bg"] = "cyan"
        self.main_button.pack_forget()
        signal_time = randint(200, 10000)
        self.after(signal_time, self.signal_user)

    def signal_user(self):
        self.start_time = time.time()
        self.info_label["text"] = "Drücke jetzt den Button!"
        self.info_label["bg"] = "green"
        self.main_button.pack()
        self.main_button["bg"] = "green"
        self.main_button["text"] = "Drück mich!"
        self.main_button["command"] = self.show_result


    def show_result(self):
        end_time = time.time()
        self.info_label["text"] = f"Du hast {end_time - self.start_time} Sekunden gebraucht"
        self.main_button.destroy()




app = Tk()
app.title("Reaktionstest")
app.geometry("400x300")
react = Reaction(app)
react.mainloop()