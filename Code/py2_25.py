import turtle as t
px, py = eval(input("请输入矩形中心坐标："))
length, width = eval(input("请输入矩形长和宽："))
t.hideturtle()
t.penup()
t.goto(px - length / 2, py + width / 2)
t.pendown()
t.goto(px + length / 2, py + width / 2)
t.goto(px + length / 2, py - width / 2)
t.goto(px - length / 2, py - width / 2)
t.goto(px - length / 2, py + width / 2)
t.mainloop()