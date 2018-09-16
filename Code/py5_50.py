import turtle as t
x = -100
y = 100
for line in range(10):
    t.penup()
    t.goto(x, y)
    t.pendown()
    x_t = x
    y_t = y
    for i in range(1, line + 2):
        t.write(str(i) + "  ", font = ("微软雅黑", 20, "normal"))
        x_t += 40
        t.penup()
        t.goto(x_t, y_t)
        t.pendown()
    y -= 30
t.hideturtle()
t.done()