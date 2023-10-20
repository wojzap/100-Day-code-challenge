from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x_cor, y_cor):
        super().__init__()

        self.x_cor = x_cor
        self.y_cor = y_cor

        self.setheading(90)
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=4, outline=None)
        self.color("blue")
        self.penup()
        self.setposition(x=x_cor, y=y_cor)


    def move_up(self):
        if self.ycor() < 245:
            self.setheading(90)
            self.forward(50)

    def move_down(self):
        if self.ycor() > -245:
            self.setheading(270)
            self.forward(50)
