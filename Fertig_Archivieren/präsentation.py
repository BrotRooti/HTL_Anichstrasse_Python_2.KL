'''
multible downloader
Phillip
11.6.22
'''

#import turtle_show
from tkinter import *
from tkinter import simpledialog, messagebox, filedialog
import random

import turtle_test

DEBUG = False


class MyApp(Frame):
    def __init__(self, master):
        super().__init__(master)
        # self.pack(fill=BOTH, expand=True)
        master.geometry("200x200")
        # frame
        self.f1 = Frame(master=master)
        self.f1.pack(fill=BOTH, expand=True)
        self.create_buttons()
        # make the grid layout expand
        for x in range(2):
            self.f1.columnconfigure(x, weight=1)
            self.f1.rowconfigure(x, weight=1)
        # make the grid layout expand


    def create_buttons(self):
        b2 = Button(master=self.f1, text="Tkinter", bg="red",
                    command=lambda: [self.tkinter_showcase(), b1.destroy(),
                                     b2.destroy(), b3.destroy(), b4.destroy()])

        b1 = Button(master=self.f1, text="Turtle", bg="purple",
                    command=lambda: [self.turtle_showcase(), b1.destroy(),
                                     b2.destroy(), b3.destroy(), b4.destroy()])

        b3 = Button(master=self.f1, text="Random", bg="orange",
                    command=lambda: [self.random_showcase(), b1.destroy(),
                                     b2.destroy(), b3.destroy(), b4.destroy(),])

        b4 = Button(master=self.f1, text="1/1", bg="green",
                    command=lambda: [self.Placeholder_download(), b1.destroy(),
                                     b2.destroy(), b3.destroy(), b4.destroy()])

        b1.grid(row=0, column=0, sticky=N + S + E + W)
        b2.grid(row=0, column=1, sticky=N + S + E + W)
        b3.grid(row=1, column=0, sticky=N + S + E + W)
        b4.grid(row=1, column=1, sticky=N + S + E + W)
        # button alignment (b1=Turtle, b2=Tkinter, b3= Randim, b4= Placeholder)

    def tkinter_showcase(self):
        if DEBUG:
            print("youtube chooser")


        empty_button = Button(master=self.f1, text="", bg="white", )
        return_button = Button(master=self.f1, text="Return", bg="green",
                               command=lambda: [self.create_buttons(),
                                                empty_button.destroy(), return_button.destroy()])


        return_button.grid(row=1, column=1, sticky=N + S + E + W)
        empty_button.grid(row=1, column=1, sticky=N + S + E + W)


    def turtle_showcase(self):
        if DEBUG:
            print("Spotify")

        empty_button = Button(master=self.f1, text="Start", bg="purple", command=self.turtle_dings)
        return_button = Button(master=self.f1, text="Return", bg="green",
                               command=lambda: [self.create_buttons(), return_button.destroy()])

        return_button.grid(row=1, column=1, sticky=N + S + E + W)
        empty_button.grid(row=0, column=0, sticky=N + S + E + W)

    def random_showcase(self):
        if DEBUG:
            print("soundcloud")

        x = random.randint(1, 69696969)
        messagebox.showinfo(title="Random Showcase", message="Ihre Zufalsszahl lautet {}".format(x))

        return_button = Button(master=self.f1, text="Return", bg="green",
                               command=lambda: [self.create_buttons(), return_button.destroy()])

        empty_button = Button(master=self.f1, text="", bg="white", )
        empty_button.grid(row=0, column=0, sticky=N + S + E + W)
        return_button.grid(row=1, column=1, sticky=N + S + E + W)

    def Placeholder_download(self):
        if DEBUG:
            print("Placeholder")



        return_button = Button(master=self.f1, text="Return", bg="green",
                               command=lambda: [self.create_buttons(), return_button.destroy()])

        return_button.grid(row=1, column=1, sticky=N + S + E + W)


    def turtle_dings(self):
        if DEBUG:
            print("turtle dings")
        turtle_test.main()

tk_window = Tk()
tk_window.title("Python Showcase")
app = MyApp(tk_window)
app.mainloop()
