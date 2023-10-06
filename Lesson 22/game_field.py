from turtle import Turtle

class GameField(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.create_field_line()


    def create_field_line(self):
        self.penup()
        self.setposition(x=0, y=-280)
        self.pendown()
        self.setheading(90)
        self.pensize(3)
        while self.ycor() < 280:
            self.forward(15)
            self.penup()
            self.forward(10)
            self.pendown()





