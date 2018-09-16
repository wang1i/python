import turtle as t
x1, y1 = eval(input("输入矩形1的中心坐标："))
width1, height1 = eval(input("输入矩形1的宽和高："))
x2, y2 = eval(input("输入矩形2的中心坐标："))
width2, height2 = eval(input("输入矩形2的宽和高："))
t.screensize(800, 600)

def drawRectangle(x, y , width, height):
    t.penup()
    t.goto(x - width / 2, y + height / 2)
    t.pendown()
    t.setx(x + width / 2)
    t.sety(y - height / 2)
    t.setx(x - width / 2)
    t.sety(y + height / 2)

drawRectangle(x1, y1, width1, height1)
drawRectangle(x2, y2, width2, height2)
t.penup()
t.goto(200, -100)
t.pendown()
if abs(x2 - x1) <= width1 / 2 - width2 / 2 and abs(y2 - y1) <= height1 / 2 - height2 / 2:
    t.write("矩形2在矩形1内")
elif abs(x2 - x1) > width1 / 2 + width2 / 2 or abs(y2 - y1) > height1 / 2 + height2 / 2:
    t.write("矩形2在矩形1外")
else:
    t.write("矩形2与矩形1相交")
t.hideturtle()
t.done()