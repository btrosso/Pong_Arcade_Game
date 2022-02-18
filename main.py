from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Rosso's Pong Game!")
screen.tracer(0)
sleep_time = 0.1

scoreboard = Scoreboard()

game_is_on = True

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")


while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    # if ball.xcor() > 380 or ball.xcor() < -380:
    #     print("hit side wall - game over")
    #     game_is_on = False

    # Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

        # if you want the ball to move faster every time it hits a paddle then uncomment the line below
        # sleep_time -= .005

    # Detect out of bounds on right
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_l_score()

    # Detect out of bounds on left
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_r_score()

    # Game over
    if scoreboard.r_score > 0 or scoreboard.l_score > 0:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
