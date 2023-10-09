import turtle
from turtle import Turtle

FINISH_LINE_Y = 280


class MyTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move(self):
        self.forward(10)

    def reset_position(self):
        self.setposition(x=0, y=-280)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

