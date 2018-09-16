import turtle as t
t.speed(10)
y = -100
dist = 10
for times in range(0, 10):
    y -= dist
    t.penup()
    t.goto(0, y)
    t.pendown()
    t.color("blue")
    t.circle(-y)

t.hideturtle()
t.done()