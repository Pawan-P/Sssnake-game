from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Sssnake Game")

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_alive = True
while is_alive:
    screen.update()
    time.sleep(0.1)

    snake.move("")
    # food
    if snake.head.distance(food) < 15:
        food.respawn()
        snake.grow()
        score.update()
    # wall collide
    if snake.head.xcor() > 285 or snake.head.xcor() > 285 or snake.head.xcor() > 285 or snake.head.xcor() > 285:
        score.print_over()
        is_alive = False
    # body collide
    for block in snake.snake_size:
        if block == snake.head:
            pass
        elif snake.head.distance(block) < 10:
            is_alive = False
            score.print_over()


screen.exitonclick()
