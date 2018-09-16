'''
import turtle as t
import math
theta = math.atan((-50 - 48) / (50 - (-39))) * (-1) * 180 / math.pi
dist = math.sqrt((50 + 39) ** 2 + (-50 - 48) ** 2)

t.penup()
t.goto(-39, 48)
t.pendown()
t.write("(-39, 48)")
t.right(theta)
t.forward(dist)
t.left(theta)
t.write("(50, -50)")
t.hideturtle()
'''
import turtle as t
t.penup()
t.goto(-39, 49)
t.pendown()
t.write("(-39, 48)")
t.goto(50, -50)
t.write("(50, -50)")
t.hideturtle()
t.mainloop()