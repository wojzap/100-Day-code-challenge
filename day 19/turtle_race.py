from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make you bet", "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


for turtle in range(0, 6):
    new_turtle = Turtle()
    new_turtle.color(colors[turtle])
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + turtle * 40)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.fillcolor()
            print(winning_color)
            if winning_color == user_bet:
                print("You've won!")
            else:
                print("You lost!")

# while is_race_on:
#     random_distance = random.randint(0,10)
#


screen.exitonclick()
