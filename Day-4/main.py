from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake GAME")
screen.tracer(0)

# colors = ["red", "green", "blue", "yellow", "orange", "purple"]

segments = []


snake = Snake()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()