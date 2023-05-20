from turtle import Turtle,Screen
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.seg = []
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for i in positions:
            self.addseg(i)

    def addseg(self,i):
        g = Turtle()
        g.color("White")
        g.shape("square")
        g.penup()
        g.goto(i)
        self.seg.append(g)

    def extent(self):
        self.addseg(self.seg[-1].position())

    def move(self):
        for i in range(len(self.seg) - 1, 0, -1):
            new_x = self.seg[i - 1].xcor()
            new_y = self.seg[i - 1].ycor()
            self.seg[i].goto(new_x, new_y)
        self.seg[0].forward(20)

    def up(self):
        if self.seg[0].heading()!=DOWN:
            self.seg[0].setheading(UP)
    def down(self):
        if self.seg[0].heading() != UP:
            self.seg[0].setheading(DOWN)
    def left(self):
        if self.seg[0].heading() != RIGHT:
            self.seg[0].setheading(LEFT)
    def right(self):
        if self.seg[0].heading() != LEFT:
            self.seg[0].setheading(RIGHT)
