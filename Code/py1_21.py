import turtle as t
t.hideturtle()
t.color("red")
t.goto(-75, 0)

t.penup()
t.goto(0, 0)
t.pendown()
t.color("blue")
t.goto(100, 0)

t.penup()
t.goto(0, 0)
t.pendown()
t.color("black")
t.goto(0, 125)

t.penup()
t.goto(-140, 0)
t.pendown()
t.write("9")

t.penup()
t.goto(140, 0)
t.pendown()
t.write("3")

t.penup()
t.goto(0, 135)
t.pendown()
t.write("12")

t.penup()
t.goto(0, -150)
t.pendown()
t.circle(150)

t.penup()
t.goto(0, -180)
t.pendown()
t.write("9:15:00")

t.mainloop()