
from turtle import Turtle, Screen

mike = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    mike.forward(10)


def move_backward():
    mike.backward(10)


def move_counter_clockwise():
    mike.left(10)
    mike.forward(10)


def move_clockwise():
    mike.right(10)
    mike.forward(10)


def clear_screen():
    screen.reset()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()