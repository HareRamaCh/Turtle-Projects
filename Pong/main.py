from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()

    # Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()

    # Right paddle misses the ball
    if ball.xcor() > 400:
        ball.home()
        ball.move_speed = 0.1
        ball.bounce_x_r_paddle()
        scoreboard.l_point()

    # Left paddle misses the ball
    if ball.xcor() < -400:
        ball.home()
        ball.move_speed = 0.1
        ball.bounce_x_l_paddle()
        scoreboard.r_point()


screen.exitonclick()
