import turtle as t
radius = eval(input("请输入正六边形外切圆半径："))
t.hideturtle()
t.penup()
t.goto(-radius, 0)
t.pendown()
t.circle(radius, steps = 6)

t.penup()
t.goto(radius, 0)
t.pendown()
t.circle(radius, steps = 6)

t.penup()
t.goto(-radius, -2 * radius)
t.pendown()
t.circle(radius, steps = 6)

t.penup()
t.goto(radius, -2 * radius)
t.pendown()
t.circle(radius, steps = 6)

t.mainloop()