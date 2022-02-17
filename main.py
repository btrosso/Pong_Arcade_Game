from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Rosso's Pong Game!")
screen.tracer(0)
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
    time.sleep(0.1)
    screen.update()
    ball.move()



screen.exitonclick()