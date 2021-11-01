from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5 , stretch_wid=0.5)
        self.random_x = random.randint(-200 , 200)
        self.random_y = random.randint(-200, 200)
        self.goto(x=self.random_x ,y=self.random_y)

    def move_food(self):
        self.random_x = random.randint(-200, 200)
        self.random_y = random.randint(-200, 200)
        self.goto(x=self.random_x, y=self.random_y)