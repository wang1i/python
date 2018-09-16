import turtle as t
t.hideturtle()
t.penup()
t.goto(0, -173)
t.pendown()
t.begin_fill()
t.fillcolor("red")
t.circle(200, steps = 6)
t.end_fill()

t.penup()
t.goto(-60, 0)
t.pendown()
t.begin_fill()
t.color("white")
t.write("STOP", font = ("微软雅黑", 40, "normal"))
t.end_fill()


t.done()
