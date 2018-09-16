import turtle as t
x0, y0 = eval(input("输入P0坐标："))
x1, y1 = eval(input("输入P1坐标："))
x2, y2 = eval(input("输入P2坐标："))
decision = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
if decision > 0:
    s = "p2在线的左边"
elif decision < 0:
    s = "p2在线的右边"
else:
    s = "p2在线上"

t.penup()
t.goto(x0, y0)
t.pendown()
t.write("p0(" + str(x0) + "," + str(y0) + ")")
t.goto(x1, y1)
t.write("p1(" + str(x1) + "," + str(y1) + ")")
t.penup()
t.goto(x2, y2)
t.pendown()
t.begin_fill()
t.fillcolor("black")
t.circle(1)
t.end_fill()
t.penup()
t.goto(x2 - 10, y2 + 10)
t.pendown()
t.write(s)

t.hideturtle()
t.done()