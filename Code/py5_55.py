import turtle as t
t.screensize(800, 600)
t.speed(10)
off = True


def drawSqure(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setx(x + 60)
    t.sety(y - 60)
    t.setx(x)
    t.sety(y)


for y in range(240, -240, -60):
    for x in range(-240, 240, 60):
        if off:
            drawSqure(x, y)
        else:
            t.begin_fill()
            t.fillcolor("black")
            drawSqure(x, y)
            t.end_fill()
        off = bool(int(off) - 1)
    off = bool(int(off) - 1)

t.hideturtle()
t.done()
