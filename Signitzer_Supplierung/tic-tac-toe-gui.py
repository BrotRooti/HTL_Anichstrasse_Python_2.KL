'''GUI Taschenrechner
17.03.2023
Phillip H.'''

from tkinter import *


class TicTacToe(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.geometry("200x200")

        self.f1 = Frame(master=master)
        self.f1.pack(fill=BOTH, expand=True)

        self.f2 = Frame(master=master)
        self.f2.pack(side='bottom', pady='5')

        self.grid_length = 3
        self.create_widgets()
        for x in range(self.grid_length):
            self.f1.columnconfigure(x, weight=1)
            self.f1.rowconfigure(x, weight=1)
        self.player = ['#ff0000', '#0000ff']

    def create_widgets(self):
        for x in range(self.grid_length):
            for y in range(self.grid_length):
                b = Button(master=self.f1,
                           text=" ",bg="#d9d9d9")
                b.bind("<ButtonPress-1>", self.TicTacToe)
                b.grid(row=y, column=x,
                       sticky=N + S + E + W)

    def check_win(self):
        pass

    #


    def TicTacToe(self, event):
        global player_number
        try:
            player_number = player_number
        except NameError:
            player_number = 0

        print(player_number)
        grid_info = event.widget.grid_info()
        column = int(grid_info['column'])
        row = int(grid_info['row'])
        if event.widget['bg'] == "#d9d9d9":
            event.widget['bg'] = self.player[player_number]
            print("Player: ", self.player[player_number])
        else:
            print("Field is already taken")
            app.mainloop()

        win = self.check_win()
        if (win ==True ):
             #Player wins
            answer = tk_window.messagebox.askyesno("Winner", "Do you want to play again?")
            if answer == True:
                self.reset()
            else:
                quit()
        if player_number == 0:
            player_number = 1
        else:
            player_number = 0


    def check_win(self,):
        playing_field = [[" " for i in range(3)] for j in range (3)]
        #if a player has 3 in a row or diagonal then return 1
        #else return 0
        for row in range(0,3,1):
            if(playing_field[0][row] == playing_field[1][row] == playing_field[2][row] != " "):
                return 1
            elif(playing_field[row][0] == playing_field[row][1] == playing_field[row][2] != " "):
                return 1
            if(playing_field[0][0] == playing_field[1][1] == playing_field[2][2] != " "):
                return 1
            elif(playing_field[2][0] == playing_field[1][1] == playing_field[0][2] != " "):
                return 1
        return 0


tk_window = Tk()
tk_window.title("Tic-Tac-Toe")
app = TicTacToe(tk_window)
app.mainloop()