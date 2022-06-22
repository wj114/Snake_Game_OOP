from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# (1) Setup a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("WenJun's Snake Game")
screen.tracer(0)

# (2) Create a snake body
snake = Snake()

# (5) Initialize food

food = Food()

# (6) Initialize score
score = Scoreboard()

# (4) Move our snake

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# (3) Move our snake

game_on = True

while game_on:
    screen.update()  # need to turn off tracer, update is like "animation" refresh
    time.sleep(0.1)

    snake.move()

    # (5) Detect collision with food
    if snake.head.distance(food) < 15:  # use "distance" method from Turtle class
        score.add_score()
        food.refresh()

        # (8) extend the snake when collide with food
        snake.extend()

    # (7) Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_scoreboard()
        snake.reset_snakeBody()

    # (8) Detect collision with tail

    for any_segment in snake.segments[1:]:  # avoid game over at the beginning as starting point is (0,0)
        if snake.head.distance(any_segment) < 10:
            score.reset_scoreboard()
            snake.reset_snakeBody()

screen.exitonclick()
