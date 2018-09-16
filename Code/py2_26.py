import turtle as t
import math
px, py, radius = eval(input("请输入圆心坐标和半径："))
area = radius**2 * math.pi
t.hideturtle()
t.penup()
t.goto(px, py)
t.pendown()
t.write(area)

t.penup()
t.goto(px, py - radius)
t.pendown()
t.circle(radius)

t.mainloop()