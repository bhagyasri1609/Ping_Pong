from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("My Pong game")
screen.tracer(0)


r_paddle=Paddle((360,0))
l_paddle=Paddle((-360,0))
ball=Ball()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"e")
screen.onkey(l_paddle.go_down,"d")

score=Score()

game_is_on=True
while game_is_on:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()
    
    if ball.ycor()> 280 or ball.ycor()< -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle)< 40 and ball.xcor()> 320 or ball.distance(l_paddle)< 40 and ball.xcor()< 320:
        ball.bounce_x()
    if ball.xcor()>380:
        score.inc_y_score()
        ball.reset_position()
    elif ball.xcor()<-380:
        score.inc_x_score()
        ball.reset_position()
    score.show_score()
    


screen.exitonclick()