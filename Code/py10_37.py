from tkinter import *
import tkinter.messagebox


class DisplayBinarySearch:
    def __init__(self):
        window = Tk()
        window.title("Binary Search Histogram")

        self.canvas = Canvas(window, width = 600, height = 500)
        self.canvas.pack()

        self.reset()
        self.low = 0
        self.high = 18
        self.mid = (self.low + self.high) // 2
        self.count = [0] * 19


        frame = Frame(window)
        frame.pack()
        Label(frame, text="Enter a key(in float):").pack(side=LEFT)
        self.v = StringVar()
        Entry(frame, textvariable=self.v, justify=RIGHT).pack(side=LEFT)
        Button(frame, text="Step", command=self.step).pack(side=LEFT)
        Button(frame, text="reset", command=self.reset).pack(side=LEFT)

        window.mainloop()

    def drawHistogram(self):
        x = 100
        y = 420
        for i in range(19):
            h = i + 1
            self.count[i] = h
            self.canvas.create_rectangle(x, y, x + 20, y - h * 20, tags="Histogram")
            self.canvas.create_text(x + 5, y - h * 20 - 10, text=str(h), tags="Histogram")
            x += 20

    def reset(self):
        try:
            self.low = 0
            self.high = 18
            self.count = [0] * 19
            self.canvas.delete("Histogram")
        except TclError:
            pass
        self.drawHistogram()

    def step(self):
        try:
            self.canvas.delete("Histogram")
        except TclError:
            pass
        self.drawHistogram()

        self.mid = (self.low + self.high) // 2
        for i in range(self.low, self.high + 1):
            self.canvas.create_rectangle(100 + i * 20, 420,
                                         120 + i * 20, 420 - self.count[i] * 20,
                                         fill="gray", tags="Histogram")
        self.canvas.create_rectangle(100 + self.mid * 20, 420,
                                     120 + self.mid * 20, 420 - self.count[self.mid] * 20,
                                     fill="black", tags="Histogram")
        if self.count[self.mid] == eval(self.v.get()):
            tkinter.messagebox.showinfo("showinfo", "the search is over")
            self.low = 0
            self.high = 18
            return
        elif self.count[self.mid] < eval(self.v.get()):
            self.low = self.mid + 1
        else:
            self.high = self.mid - 1


if __name__ == '__main__':
    DisplayBinarySearch()
