from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("gra w wenrza")
screen.tracer(0)

screen.listen()

snake = Snake()

screen.onkey(key="w", fun=snake.go_up)
screen.onkey(key="s", fun=snake.go_down)
screen.onkey(key="a", fun=snake.go_left)
screen.onkey(key="d", fun=snake.go_right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()