from tkinter import *

class BarChart:
    def __init__(self):
        window = Tk()
        window.title("条状图")

        canvas = Canvas(window, width = 500, height = 400)
        canvas.place(x = 100, y = 60)

        canvas.create_line(0, 300, 500, 300)
        canvas.create_rectangle(20, 300, 120, 200, fill = "black")
        canvas.create_rectangle(140, 300, 240, 250, fill = "black")
        canvas.create_rectangle(260, 300, 360, 220, fill = "brown")
        canvas.create_rectangle(380, 300, 480, 180, fill = "brown")

        Label(canvas, text = "课题 --20%").place(x = 30, y = 170)
        Label(canvas, text="测验 --10%").place(x=150, y=220)
        Label(canvas, text="期中考试 --30%").place(x=270, y=190)
        Label(canvas, text="期末考试 --40%").place(x=390, y=150)
        window.mainloop()

BarChart()