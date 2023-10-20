from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("gra w wenrza")
screen.tracer(0)

screen.listen()

snake = Snake()
food = Food()
score = Score()

screen.onkey(key="w", fun=snake.go_up)
screen.onkey(key="s", fun=snake.go_down)
screen.onkey(key="a", fun=snake.go_left)
screen.onkey(key="d", fun=snake.go_right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 20:
        food.new_location()
        snake.extend()
        score.add_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()