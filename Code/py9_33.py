from tkinter import *
import random as r


class RandomLine:
    def __init__(self):
        window = Tk()
        window.title("Random an Arrow Line")

        frame1 = Frame(window)
        frame1.pack()
        self.canvas = Canvas(frame1, width = 500, height = 400)
        self.canvas.pack()

        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, text = "Draw a Random Arrow Line", command = self.drawLine).pack()

        window.mainloop()

    def drawLine(self):
        try:
            self.canvas.delete("line")
        except TclError:
            pass
        self.canvas.create_line(r.random() * 480, r.random() * 380, r.random() * 480, r.random() * 380,
                                arrow = "last", activefill = "blue",tags = "line")


if __name__ == '__main__':
    RandomLine()