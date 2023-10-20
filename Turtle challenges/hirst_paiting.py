import random
from colors_extraction import colors
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

mike = Turtle()
mike.hideturtle()
mike.speed("fastest")
mike.shape("circle")
mike.penup()

for row in range(10):
    mike.setheading(90)
    mike.forward(50 * row)
    mike.setheading(0)
    for column in range(10):
        mike.color(random.choice(colors))
        mike.stamp()
        mike.forward(50)
    mike.home()



screen.exitonclick()