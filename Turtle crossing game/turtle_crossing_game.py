from turtle import Screen
from my_turtle import MyTurtle
from car import Car
from score import Scoreboard
import time

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

turtle = MyTurtle()
screen.onkeypress(key="w", fun=turtle.move)
car = Car()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()

    car.spawn_car()
    car.move_cars()
    for random_car in car.cars:
        if random_car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.is_at_finish_line():
        turtle.reset_position()
        scoreboard.increase_level()
        car.level_up()


screen.exitonclick()