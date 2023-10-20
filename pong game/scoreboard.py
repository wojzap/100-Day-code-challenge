from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.score_update(self.player)

    def score_update(self, player):
        self.clear()
        if player == 1:
            self.setposition(x=-60, y=230)
            self.write(arg=f"{self.score}", move=False, align="center", font=("Arial", 35, "normal"))
        elif player == 2:
            self.setposition(x=60, y=230)
            self.write(arg=f"{self.score}", move=False, align="center", font=("Arial", 35, "normal"))

    def add_score(self):
        self.score += 1
        self.score_update(self.player)
