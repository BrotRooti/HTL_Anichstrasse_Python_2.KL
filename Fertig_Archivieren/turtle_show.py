'''
Exploring Python turtle
Julian, Phillip
02.05.2022
'''

#importing classes
import turtle
from turtle import *
import time


#
# Functions
#

# Draws a square
def square(size):
    for i in range(4):
        forward(size)
        left(90)

# Draws a rectangle
def rectangle(a, b):
    for i in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)

# Moves the turtle without a line behind it
def move(x, y):
    penup()
    turtle.hideturtle()
    goto(x, y)
    setheading(0)
    turtle.showturtle()
    pendown()

# ends fill - changes color - starts new fill
def colorchange(pencolor, fillcolor):
    end_fill()
    color(pencolor, fillcolor)
    begin_fill()

# Draws the House at given coords with given colors
def house(startx, starty, pencolor, fillcolor, scale):
    move(startx, starty)
    colorchange(pencolor, fillcolor)

    speed(1)
    square(100*scale)

    move(xcor() + 100*scale, ycor() + 100*scale)
    left(135)
    forward(70.711*scale)
    left(90)
    forward(70.711*scale)

    colorchange(pencolor, '#00fcf0')
    move(xcor() + 15*scale, ycor() - 30*scale)
    square(20*scale)

    colorchange(pencolor, '#00fcf0')
    move(xcor() + 50*scale, ycor())
    square(20*scale)

    colorchange(pencolor, '#593323')
    move(xcor() - 15*scale, ycor() - 70*scale)
    rectangle(20*scale, 40*scale)

    colorchange('#fffb00', '#fffb00')
    move(xcor() + 3*scale, ycor() + 15*scale)
    circle(2.5*scale)

    end_fill()


def main():
    #messages and input
    X = -180
    Y = -250
    scale = 4


    #change the rgb values to hex
    pencolor = '#05B3FF'
    fillcolor = '#FF05B3'

    #draws the house
    house(X, Y, pencolor, fillcolor, scale)


def hauptroutine():
    main()
    time.sleep(2.5)

