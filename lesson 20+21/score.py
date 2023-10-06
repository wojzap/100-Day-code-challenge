from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
GAME_OVER_FONT = ("Arial", 30, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.refresh()

    def add_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)
