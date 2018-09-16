import turtle as t
t.screensize(1000, 600)

t.penup()
t.goto(-800, -100)
t.pendown()
t.left(60)
t.circle(100, steps = 3)
t.right(60)

t.penup()
t.goto(-500, -100)
t.pendown()
t.circle(100, steps = 4)

t.penup()
t.goto(-200, -100)
t.pendown()
t.circle(100, steps = 5)

t.penup()
t.goto(100, -100)
t.pendown()
t.circle(100, steps = 6)

t.penup()
t.goto(400, -200)
t.pendown()
t.circle(100, steps = 7)

t.done()