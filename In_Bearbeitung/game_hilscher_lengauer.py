from tkinter import *
from tkinter import messagebox
from random import *
from time import sleep, time
from math import sqrt


class BubbleBlaster:
    def __init__(self):
        self.H = 500
        self.B = 800
        self.window = Tk()
        self.window.title("Bubble Blaster")
        self.c = Canvas(self.window, width=self.B, height=self.H, bg="darkblue")
        self.c.pack()

        # U-Boot zeichnen
        self.img = PhotoImage(file="uboot.png")
        self.uboot = self.c.create_image(self.B / 2, self.H / 2, image=self.img)
        self.UBOOT_R = 45

        # U-Boot steuern
        self.UBOOT_GESCHW = 10
        self.c.bind_all("<Key>", self.uboot_bewegen)

        # Bubbles erzeugen
        self.bubble_img = PhotoImage(file="bubble.png")
        self.special_bubble_img = PhotoImage(file="bubble_special.png")
        self.BUB_R = 25
        self.bub_id = []
        self.bub_geschw = []
        self.MAX_BUB_GESCHW = 10
        self.GAP = 100

        # Zeit und Punkte anzeigen
        self.time_text = self.c.create_text(50, 50, fill="white")
        self.score_text = self.c.create_text(150, 50, fill="white")

        # Hauptschleife
        self.score = 0
        self.TIME_LIMIT = 30
        self.ende = time() + self.TIME_LIMIT

    def start(self):
        while time() < self.ende:
            if randint(1, 10) == 1:
                self.erzeuge_bubble()
            self.bewege_bubbles()
            self.entferne_bubbles()
            self.score += self.treffer()
            self.zeige_punkte()
            self.zeige_zeit()
            self.window.update()
            sleep(0.01)

        self.c.create_text(
            self.B / 2,
            self.H / 2,
            text="GAME OVER",
            fill="white",
            font=("Helvetica", 30),
            tag="tag1",
        )
        self.c.create_text(
            self.B / 2,
            self.H / 2 + 30,
            text="Punkte: " + str(self.score),
            fill="white",
            tag="tag2",
        )
        self.neustart()


    def uboot_bewegen(self, event):
        x, y = self.c.coords(self.uboot)
        if event.keysym == "Up":
            if y >= self.UBOOT_GESCHW:
                self.c.move(self.uboot, 0, -self.UBOOT_GESCHW)
        elif event.keysym == "Down":
            if y <= self.H - self.UBOOT_GESCHW:
                self.c.move(self.uboot, 0, self.UBOOT_GESCHW)
        elif event.keysym == "Left":
            if x >= self.UBOOT_GESCHW:
                self.c.move(self.uboot, -self.UBOOT_GESCHW, 0)
        elif event.keysym == "Right":
            if x <= self.B - self.UBOOT_GESCHW:
                self.c.move(self.uboot, self.UBOOT_GESCHW, 0)

    def erzeuge_bubble(self):
        x = self.B + self.GAP
        y = randint(0, self.H)
        v = randint(1, self.MAX_BUB_GESCHW)
        if randint(1, 20) == 1:
            id_num = self.c.create_image(x, y, image=self.special_bubble_img)
        else:
            id_num = self.c.create_image(x, y, image=self.bubble_img)
        self.bub_id.append(id_num)
        self.bub_geschw.append(v)

    def bewege_bubbles(self):
        for i in range(len(self.bub_id)):
            self.c.move(self.bub_id[i], -self.bub_geschw[i], 0)

    def lösche_bubble(self, i):
        self.c.delete(self.bub_id[i])
        del self.bub_id[i]
        del self.bub_geschw[i]

    def entferne_bubbles(self):
        for i in range(len(self.bub_id) - 1, -1, -1):
            x, y = self.c.coords(self.bub_id[i])
            if x < -self.GAP:
                self.lösche_bubble(i)

    def abstand(self, uboot, id_bubble):
        x1, y1 = self.c.coords(uboot)
        x2, y2 = self.c.coords(id_bubble)
        a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return a

    def treffer(self):
        punkte = 0
        for i in range(len(self.bub_id) - 1, -1, -1):
            if self.abstand(self.uboot, self.bub_id[i]) < (self.UBOOT_R + self.BUB_R):
                punkte += (self.BUB_R + self.bub_geschw[i])
                self.lösche_bubble(i)
        return punkte

    def zeige_punkte(self):
        self.c.itemconfig(self.score_text, text="Punkte: " + str(self.score))

    def zeige_zeit(self):
        self.c.itemconfig(
            self.time_text, text="Zeit: " + str(int(self.ende - time()))
        )

    def neustart(self):
        antwort = messagebox.askyesno(title="Game Over", message="Wollen sie nochmal spielen?")

        if antwort:
            self.ende = time() + self.TIME_LIMIT
            self.score = 0
            self.c.delete("tag1")
            self.c.delete("tag2")
            self.start()
        else:
            raise SystemExit


game = BubbleBlaster()
while True:
    try:
        if __name__ == "__main__":
            game.start()
    except SystemExit:
        quit()
