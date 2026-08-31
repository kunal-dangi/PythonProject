from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
screen = Screen()
screen.tracer(0)

screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.title("Pong Game")
paddle1 = Paddle(370, 0)
paddle2 = Paddle(-370, 0)
ball = Ball()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")


game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.xcor() > 250 and ball.distance(paddle1) < 60 or ball.xcor() < -250 and ball.distance(paddle2) < 60:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.reset_position ()
        scoreboard.point_1()


    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.point_2()


screen.exitonclick()