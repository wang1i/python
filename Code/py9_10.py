from tkinter import *

class PieChart:
    def __init__(self):
        window = Tk()
        window.title("饼状图")

        canvas = Canvas(window, width = 500, height = 500)
        canvas.place(x = 0, y = 0)
        Message(canvas, text="课题 -- 20%").place(x=250, y=110)

        canvas.create_arc(100, 300, 300, 100, start = 0, extent = 72, fill = "red", tags = "arc")
        canvas.create_arc(100, 300, 300, 100, start=72, extent=36, fill="yellow", tags="arc")
        canvas.create_arc(100, 300, 300, 100, start=108, extent=108, fill="blue", tags="arc")
        canvas.create_arc(100, 300, 300, 100, start=216, extent=144, fill="green", tags="arc")



        window.mainloop()

PieChart()