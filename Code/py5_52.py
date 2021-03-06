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
'''绘制曲线'''
t.penup()
t.goto(-175, 50 * math.sin((-175 / 100) * 2 * math.pi))
t.pendown()
for x in range(-175, 176):
    t.goto(x , 50 * math.sin((x / 100) * 2 * math.pi))

t.hideturtle()
t.done()