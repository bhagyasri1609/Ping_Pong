from turtle import Turtle
class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.x_score=0
        self.y_score=0
        
    
    def inc_x_score(self):
        self.x_score+=1
    def inc_y_score(self):
        self.y_score+=1
    
    def show_score(self):
        self.clear()
        self.goto(100,200)
        self.write(f"{self.x_score}",move=False,align="center",font=("Courier",50,"normal"))
        self.goto(-100,200)
        self.write(f"{self.y_score}",move=False,align="center",font=("Courier",50,"normal"))
