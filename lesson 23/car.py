from turtle import Turtle
import random



class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.car_speed = 10

    def spawn_car(self):
        number = random.randint(0, 2)
        if number == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.setheading(180)
            new_car.shape("square")
            new_car.turtlesize(stretch_len=2)
            y_cor = random.randint(-280, 280)
            new_car.setposition(x=300, y=y_cor)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            random_color = (r, g, b)
            new_car.color(random_color)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += 10




