import turtle as t
t.hideturtle()
t.penup()
t.goto(0, 0)
t.pendown()
t.goto(100, 0)
t.goto(100, -50)
t.goto(0, -50)
t.goto(0, 0)

t.penup()
t.goto(-25, -25)
t.pendown()
t.goto(75, -25)
t.goto(75, -75)
t.goto(-25, -75)
t.goto(-25, -25)

t.penup()
t.goto(0, 0)
t.pendown()
t.goto(-25, -25)

t.penup()
t.goto(100, 0)
t.pendown()
t.goto(75, -25)

t.penup()
t.goto(0, -50)
t.pendown()
t.goto(-25, -75)

t.penup()
t.goto(100, -50)
t.pendown()
t.goto(75, -75)

t.mainloop()