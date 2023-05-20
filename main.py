import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Welcome to snake game")

sn=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(key="Up",fun=sn.up)
screen.onkey(key="Down",fun=sn.down)
screen.onkey(key="Left",fun=sn.left)
screen.onkey(key="Right",fun=sn.right)
game=True
while game is True:
    screen.update()
    time.sleep(0.1)
    sn.move()
    #Detect collision with food
    if sn.seg[0].distance(food)<15:
        food.refresh()
        score.inre()
        sn.extent()
    #Detect collision with wall
    if sn.seg[0].xcor()>280 or sn.seg[0].xcor()<-300 or sn.seg[0].ycor()>300 or sn.seg[0].ycor()<-280:
        score.over()
        game=False
    #Detect collision with body
    for i in sn.seg[1:]:
        if sn.seg[0].distance(i)<10:
            score.over()
            game=False

screen.exitonclick()
