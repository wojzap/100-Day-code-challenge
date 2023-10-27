from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
GAME_OVER_FONT = ("Arial", 30, "normal")




class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"C:\Users\Dragon\Desktop\Python 100 days chall\Learning\Snake game\data.txt", mode="r") as data:
            self.high_score = int(data.read())
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
        self.write(arg=f"Score: {self.score} High_score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"C:\Users\Dragon\Desktop\Python 100 days chall\Learning\Snake game\data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.refresh()



