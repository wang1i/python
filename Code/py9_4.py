from tkinter import *

class DisplayRectangle:
    def __init__(self):
        window = Tk()
        window.title("Display Rectangle")

        canvas = Canvas(window, width = 800, height = 600, bg = "white")
        canvas.pack()

        x1 = 300
        y1 = 300
        x2 = 500
        y2 = 320

        for _ in range(20):
            x1 -= 10
            y1 += 10
            x2 += 10
            y2 -= 10
            canvas.create_rectangle(x1, y1, x2, y2)

        window.mainloop()

DisplayRectangle()