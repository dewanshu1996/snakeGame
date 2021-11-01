import time
from turtle import Turtle, Screen
import random
from snake import Snake
from food import Food
from scoreboard import Scoreboard

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake game 101")
window.tracer(0)
snake = Snake()
window.listen()
window.onkey(key="Up", fun=snake.up)
window.onkey(key="Down", fun=snake.down)
window.onkey(key="Left", fun=snake.left)
window.onkey(key="Right", fun=snake.right)

game_is_on = True
window.update()
food = Food()
scoreboard = Scoreboard()

while game_is_on:
    snake.move_snake()
    time.sleep(0.1)
    window.update()

    if snake.snake_head.distance(food) < 15:
        food.move_food()
        scoreboard.increment_score()
        snake.extend_snake_body()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 \
            or snake.snake_head.ycor() > 280 \
            or snake.snake_head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.snake_body:
        if segment == snake.snake_head:
            pass
        else:
            if segment.distance(snake.snake_head) < 10:
                game_is_on = False
                scoreboard.game_over()

window.exitonclick()
