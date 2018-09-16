import turtle as t
t.screensize(800, 600)
for y in range(180, -200, -20):
   t.penup()
   t.goto(-180, y)
   t.pendown()
   t.setx(180)
for x in range(-180, 200, 20):
   t.penup()
   t.goto(x, 180)
   t.pendown()
   t.sety(-180)
t.hideturtle()
t.done()

