from turtle import Turtle, Screen
import random

mike = Turtle()
screen = Screen()
screen.colormode(255)


directions = [0, 90, 180, 270]
mike.speed("fastest")
def random_color(turtle):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    turtle.color(r, g, b)

# for i in range(20000):
#     random_color(mike)
#     mike.forward(30)
#     mike.setheading(random.choice(directions))


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        random_color(mike)
        mike.circle(90)
        mike.right(size_of_gap)


draw_spirograph(5)


screen.exitonclick()


