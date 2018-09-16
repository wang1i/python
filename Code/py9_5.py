from tkinter import *

class DisplayCheckboard:
    def __init__(self):
        window = Tk()
        window.title("Display Checkboard")

        canvas = Canvas(window, width = 800, height = 800)
        canvas.pack()

        x1 = 0

        white = True
        for dx in range(8):
            x1 += 50
            y1 = 0
            for dy in range(8):
                y1 += 50
                x2 = x1 + 50
                y2 = y1 - 50

                if white:
                    canvas.create_rectangle(x1, y1, x2, y2, fill = "white", tags = "rect")
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="black", tags="rect")
                white = bool(white - 1)
            white = bool(white - 1)

        window.mainloop()

DisplayCheckboard()

