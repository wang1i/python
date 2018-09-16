import turtle as t
radius = eval(input("请输入半径："))
t.pensize(8)
t.speed(10)

t.penup()
t.goto(-2 * radius - 30 , 0)
t.pendown()
t.color("blue")
t.circle(radius)

t.penup()
t.goto(0 , 0)
t.pendown()
t.color("black")
t.circle(radius)


t.penup()
t.goto(2 * radius + 30 , 0)
t.pendown()
t.color("red")
t.circle(radius)

t.penup()
t.goto(-radius - 20, -radius)
t.pendown()
t.color("yellow")
t.circle(radius)

t.penup()
t.goto(radius + 20, -radius)
t.pendown()
t.color("green")
t.circle(radius)

t.hideturtle()
t.done()