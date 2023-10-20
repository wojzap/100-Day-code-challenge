from turtle import Turtle
import random
HEADINGS = [45, 135, 225, 315]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.setheading(random.choice(HEADINGS))
        self.move_speed = 0.05


    def move(self):
        self.forward(10)

    def wall_bounce(self):
        if self.heading() == 45:
            self.setheading(315)
        elif self.heading() == 315:
            self.setheading(45)
        elif self.heading() == 225:
            self.setheading(135)
        elif self.heading() == 135:
            self.setheading(225)

    def paddle_bounce(self):
        if self.heading() == 315:
            self.setheading(225)
        elif self.heading() == 225:
            self.setheading(315)
        elif self.heading() == 45:
            self.setheading(135)
        elif self.heading() == 135:
            self.setheading(45)
        self.move_speed *= 0.9


    def set_on_middle(self):
        self.setposition(0, 0)
        self.move_speed = 0.05
        self.setheading(random.choice(HEADINGS))

