import turtle as t
import random as r
def createRandomPoint(width, height):
    x = r.random() * width - width / 2
    y = r.random() * height - height / 2
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.circle(1)
    t.end_fill()

t.penup()
t.goto(-60, 50)
t.pendown()
t.setx(60)
t.sety(-50)
t.setx(-60)
t.sety(50)

for _ in range(10):
    createRandomPoint(120, 100)

t.hideturtle()
t.done()