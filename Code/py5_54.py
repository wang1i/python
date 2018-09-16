import turtle as t
import math
'''绘制x轴'''
t.penup()
t.goto(-190, 0)
t.pendown()
t.goto(190, 0)
t.goto(185, 5)
t.penup()
t.goto(190, 0)
t.pendown()
t.goto(185, -5)
'''绘制y轴'''
t.penup()
t.goto(0, -140)
t.pendown()
t.goto(0, 140)
t.goto(-5, 135)
t.penup()
t.goto(0, 140)
t.pendown()
t.goto(5, 135)

t.penup()
t.goto(-150, 150)
t.pendown()
for x in range(-150, 160):
    t.goto(x, x**2 / 150)

t.hideturtle()
t.done()