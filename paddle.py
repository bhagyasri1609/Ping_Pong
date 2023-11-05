from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def go_up(self):
        paddle_y=self.ycor()+20
        self.goto(self.xcor(),paddle_y)
    def go_down(self):
        paddle_y=self.ycor()-20
        self.goto(self.xcor(),paddle_y)