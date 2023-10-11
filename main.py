from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by @Emilio_Morles")
screen.tracer(0)  # https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:  # It detects collision with food
        food.refresh()  # The food appears in another random place everytime the snake eats it.
        # snake.create_snake()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 295 or snake.head.ycor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -295:
        # It detects collision with a wall.
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:  # It detects collision with its own tail.

            scoreboard.reset()
            snake.reset()

screen.exitonclick()
