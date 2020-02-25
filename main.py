import turtle
import random
from turtle import *
colors = ["red", "blue", "green", "yellow", "black"]
tim = turtle.Turtle()
tim.speed(0)
tim.width(5)

def up():
    tim.setheading(90)
    tim.forward(100)

def down():
    tim.setheading(270)
    tim.forward(100)

def left():
    tim.setheading(180)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)


def click_left(x, y):
    tim.color(random.choice(colors))
def happy():
    print("j")
    tim.write("j", font=("Comic Sans", 24, "normal"))

turtle.listen()
turtle.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(happy, "j")

turtle.onscreenclick(click_left, 1)


turtle.mainloop()
