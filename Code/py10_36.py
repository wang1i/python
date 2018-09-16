from tkinter import *
import random as r
import tkinter.messagebox


class LinearSearch:
    def __init__(self):
        self.count = [0] * 20
        self.step = -1
        self.x = 100
        self.y = 420

        window = Tk()
        window.title("Linear Search Animation")

        self.canvas = Canvas(window, width = 600, height = 450)
        self.canvas.pack()
        self.createHistogram()

        frame = Frame(window)
        frame.pack()
        Label(frame, text = "Enter a key(in float):").pack(side = LEFT)
        self.v = StringVar()
        Entry(frame, textvariable = self.v, justify = RIGHT).pack(side = LEFT)
        Button(frame, text = "Step", command = self.search).pack(side = LEFT)
        Button(frame, text = "reset", command = self.createHistogram).pack(side = LEFT)

        window.mainloop()

    def createHistogram(self):
        try:
            self.step = -1
            self.x = 100
            self.count = [0] * 20
            self.canvas.delete("histogram")
        except TclError:
            pass
        x = 100
        y = 420
        for i in range(20):
            h = int(r.random() * 20) + 1
            self.count[i] += h
            self.canvas.create_rectangle(x, y, x + 20, y - h * 20, tags = "histogram")
            self.canvas.create_text(x + 5, y - h * 20 - 10, text = str(h), tags = "histogram")
            x += 20

    def search(self):
        if self.x == 500:
            self.x = 100
        self.step += 1
        if self.step == 20:
            tkinter.messagebox.showinfo("showinfo", "the search is over")
            self.step = 0
        if self.count[self.step] == eval(self.v.get()):
            self.canvas.create_rectangle(self.x, self.y, self.x + 20, self.y - self.count[self.step] * 20,
                                             fill = "black", tags = "histogram")
        else:
            self.canvas.create_rectangle(self.x, self.y, self.x + 20, self.y - self.count[self.step] * 20,
                                             fill = "gray", tags = "histogram")
        self.x += 20


if __name__ == '__main__':
    LinearSearch()
