from turtle import *

def main():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    bgcolor("black")
    speed(5)
    for x in range(360):
        pencolor(colors[x % 6])
        width(x / 100 + 1)
        forward(x)
        left(59)

    hideturtle()
    done()