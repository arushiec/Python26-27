#myfunctions

import turtle

bob = turtle.Turtle()

def polygon(distance, sides, c):
    bob.color(c)
    angle=360 / sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def jump (x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()
