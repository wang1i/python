from tkinter import *

class DisplayGrid:
    def __init__(self):
        window = Tk()
        window.title("drawGrid")

        canvas = Canvas(window, width = 600, height = 600)
        canvas.pack()

        for x in range(70, 471, 50):
            canvas.create_line(x, 20, x, 520, tags = "line")
        for y in range(70, 471, 50):
            canvas.create_line(20, y, 520, y, tags = "line")

        window.mainloop()

DisplayGrid()

