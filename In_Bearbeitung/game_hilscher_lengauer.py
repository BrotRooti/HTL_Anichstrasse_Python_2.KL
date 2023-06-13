from tkinter import *
from random import *
from time import sleep, time
from math import sqrt


class Main(Frame):

    def __int__(self, c, master=None):
        super().__init__(master)


        self.H = 500
        self.B = 800
        #
        c.pack()
        c.bind_all("<Key>", self.uboot_bewegen)

        self.assigner(c)

    def assigner(self, c):
        img = PhotoImage(file="uboot.png")
        self.uboot = c.create_image(self.B / 2, self.H / 2, image=img)
        self.bubble_img = PhotoImage(file="bubble.png")
        self.UBOOT_R = 45
        self.UBOOT_GESCHW = 10
        self.BUB_R = 25
        self.bub_id = []
        self.bub_geschw = []
        self.MAX_BUB_GESCHW = 10
        self.GAP = 100
        self.create_ui(c)
        self.game_loop(c)

    def create_ui(self, c):
        c.create_text(50, 30, text="ZEIT", fill="white")
        c.create_text(150, 30, text="PUNKTE", fill="white")
        self.time_text = c.create_text(50, 50, fill="white")
        self.score_text = c.create_text(150, 50, fill="white")
        c.pack()

    def game_over(self, c):
        c.create_text(self.B / 2, self.H / 2, text="GAME OVER", fill="white", font=("Helvetica", 30))
        c.create_text(self.B / 2, self.H / 2 + 30, text="Punkte: " + str(self.score), fill="white")

    def zeige_punkte(self, score, c):
        c.itemconfig(self.score_text, text=str(score))

    def zeige_zeit(self, time_left, c):
        c.itemconfig(self.time_text, text=str(time_left))

    def game_loop(self, c):
        self.score = 0
        TIME_LIMIT = 30
        ende = time() + TIME_LIMIT
        while time() < ende:
            if randint(1, 10) == 1:
                self.erzeuge_bubble(c)
            self.bewege_bubbles(c)
            self.entferne_bubbles(c)
            self.score += self.treffer(c)
            self.zeige_punkte(self.score,c)
            self.zeige_zeit(int(ende - time()),c)
            app.update()
            sleep(0.01)
        self.game_over(c)

    def uboot_bewegen(self, event, c):
        x, y = c.coords(self.uboot)
        if event.keysym == "Up":
            if y >= self.UBOOT_GESCHW:
                c.move(self.uboot, 0, -self.UBOOT_GESCHW)
        elif event.keysym == "Down":
            if y <= self.H - self.UBOOT_GESCHW:
                c.move(self.uboot, 0, self.UBOOT_GESCHW)
        elif event.keysym == "Left":
            if x >= self.UBOOT_GESCHW:
                c.move(self.uboot, -self.UBOOT_GESCHW, 0)
        elif event.keysym == "Right":
            if x <= self.B - self.UBOOT_GESCHW:
                c.move(self.uboot, self.UBOOT_GESCHW, 0)

    def treffer(self, c):
        punkte = 0
        for i in range(len(self.bub_id) - 1, -1, -1):
            if self.abstand(self.uboot, self.bub_id[i],c) < (self.UBOOT_R + self.BUB_R):
                punkte += (self.BUB_R + self.bub_geschw[i])
                self.lösche_bubble(i, c)
        return punkte

    def erzeuge_bubble(self, c):
        x = self.B + self.GAP
        y = randint(0, self.H)
        v = randint(1, self.MAX_BUB_GESCHW)
        id_num = c.create_image(x, y, image=self.bubble_img)
        self.bub_id.append(id_num)
        self.bub_geschw.append(v)

    def bewege_bubbles(self, c):
        for i in range(len(self.bub_id)):
            c.move(self.bub_id[i], -self.bub_geschw[i], 0)

    def lösche_bubble(self, i, c):
        c.delete(self.bub_id[i])
        del self.bub_id[i]
        del self.bub_geschw[i]

    def entferne_bubbles(self, c):
        for i in range(len(self.bub_id) - 1, -1, -1):
            x, y = c.coords(self.bub_id[i])
            if x < -self.GAP:
                self.lösche_bubble(i, c)

    def abstand(self, uboot, id_bubble, c):
        x1, y1 = c.coords(uboot)
        x2, y2 = c.coords(id_bubble)
        a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return a


app = Tk()
app.title("Bubble Blaster")
c = Canvas(app, width=500, height=800, bg="darkblue")
# Aktivierung des Fensters
main = Main(c)
main.mainloop()
