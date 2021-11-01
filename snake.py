from turtle import Turtle, Screen
import random

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.initialise_snake_body()
        self.snake_head = self.snake_body[0]

    def initialise_snake_body(self):
        for i in range(0, 3):
            turtle = Turtle();
            turtle.penup()
            turtle.color("white")
            turtle.shape("square")
            turtle.width("small")

            if i == 0:
                turtle.setposition(x=0, y=0)
            else:
                new_x_cor = self.snake_body[-1].xcor() - 20
                turtle.setposition(x=new_x_cor, y=0)
            self.snake_body.append(turtle)

    def move_snake(self, displacement=110):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x_cor = self.snake_body[i - 1].xcor()
            new_y_cor = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x=new_x_cor, y=new_y_cor)

        self.snake_body[0].forward(20)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def extend_snake_body(self):
        turtle = Turtle();
        turtle.penup()
        turtle.color("white")
        turtle.shape("square")
        turtle.width("small")
        turtle.goto(self.snake_body[-1].position())
        self.snake_body.append(turtle)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)