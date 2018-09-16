from tkinter import *
import math


class TwoCircles:
    def __init__(self):
        window = Tk()
        window.title("Two Circles")

        self.x1 = 100.
        self.y1 = 100.
        self.x2 = 300.
        self.y2 = 200.

        self.canvas = Canvas(window, width = 400, height = 300)
        self.canvas.pack()
        self.canvas.bind("<B1- Motion>", self.moveTwoCircles)

        self.drawTwoCircles()

        window.mainloop()

    def drawTwoCircles(self):
        self.canvas.create_oval(self.x1 - 20, self.y1 - 20, self.x1 + 20, self.y1 + 20,
                                fill="black", tags="circles")
        self.canvas.create_oval(self.x2 - 20, self.y2 - 20, self.x2 + 20, self.y2 + 20,
                                fill="black", tags="circles")
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, tags="circles")
        self.canvas.create_text((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2,
                                text = format(math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2),
                                              ".2f"), tags = "circles")

    def moveTwoCircles(self, event):
        if math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) > 70:
            if math.sqrt((event.x - self.x1) ** 2 + (event.y - self.y1) ** 2) < 10:
                try:
                    self.canvas.delete("circles")
                except TclError:
                    pass
                self.x1 = event.x
                self.y1 = event.y
                self.drawTwoCircles()
            if math.sqrt((event.x - self.x2) ** 2 + (event.y - self.y2) ** 2) < 10:
                try:
                    self.canvas.delete("circles")
                except TclError:
                    pass
                self.x2 = event.x
                self.y2 = event.y
                self.drawTwoCircles()

TwoCircles()





