from tkinter import *
import random as r


class CountLetters:
    def __init__(self):
        self.count = 26 * [0]
        window = Tk()
        window.title("count of each letters")

        self.canvas = Canvas(window, width = 800, height = 500)
        self.canvas.pack()

        Button(window, text = "Display Histogram", command = self.drawHistogram).pack()

        window.mainloop()

    def drawHistogram(self):
        try:
            self.canvas.delete("histogram")
        except TclError:
            pass
        x = 100
        y = 400
        for _ in range(1000):
            self.count[int(r.random() * 26)] += 1
        for i in range(26):
            self.canvas.create_text(x + 8, y + 10, text = chr(ord('a') + i), tags = "histogram")
            self.canvas.create_rectangle(x, y, x + 20, y - self.count[i] * 5, tags = "histogram")
            self.canvas.create_text(x + 8, y - self.count[i] * 5 - 10,
                                    text = str(self.count[i]), tags="histogram")
            x += 20
        self.count = 26 * [0]

CountLetters()