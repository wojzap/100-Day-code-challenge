from turtle import Screen
from game_field import GameField
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.title("Padle game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

game_field = GameField()

paddle_left = Paddle(x_cor=-350, y_cor=0)
paddle_right = Paddle(x_cor=350, y_cor=0)

score_board_one = ScoreBoard(1)
score_board_two = ScoreBoard(2)

ball = Ball()

screen.onkeypress(key="w", fun=paddle_left.move_up)
screen.onkeypress(key="s", fun=paddle_left.move_down)
screen.onkeypress(key="Up", fun=paddle_right.move_up)
screen.onkeypress(key="Down", fun=paddle_right.move_down)

game_is_on = True
while game_is_on:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    if ball.xcor() < -380:
        score_board_two.add_score()
        ball.set_on_middle()
    if ball.xcor() > 380:
        score_board_one.add_score()
        ball.set_on_middle()
    if (ball.distance(paddle_right) < 50 and ball.xcor() > 330
            or ball.distance(paddle_left) < 50 and ball.xcor() < -330):
        ball.paddle_bounce()

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


screen.exitonclick()