from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.score()

    def score(self):
        self.k=0
        self.write(arg=f"Score = {self.k}", align="center", font=("Arial",24,"normal"))
    def inre(self):
        self.clear()
        self.k+=1
        self.write(arg=f"Score = {self.k}", align="center",font=("Arial",24,"normal"))
    def over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=("Arial", 24, "normal"))
