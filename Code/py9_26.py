from tkinter import *
import random as r


class RandomBalls:
    def __init__(self):
        window = Tk()
        window.title("Random Balls")

        self.canvas = Canvas(window, width = 600, height = 400)
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Button(frame, text = "Display", command = self.display_balls).pack()

        window.mainloop()

    def display_balls(self):
        try:
            self.canvas.delete("ball")
        except TclError:
            pass
        for _ in range(10):
            x = r.random() * 590
            y = r.random() * 390
            self.canvas.create_oval(x, y, x + 10, y + 10, fill = "black", tags = "ball")

RandomBalls()