import turtle as t
radius = eval(input("请输入半径："))
t.hideturtle()
t.penup()
t.goto(-radius, 0)
t.pendown()
t.circle(radius)

t.penup()
t.goto(radius, 0)
t.pendown()
t.circle(radius)

t.penup()
t.goto(-radius, -2 * radius)
t.pendown()
t.circle(radius)

t.penup()
t.goto(radius, -2 * radius)
t.pendown()
t.circle(radius)

t.mainloop()