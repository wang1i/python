from tkinter import *
import random


class SelectSort:
    def __init__(self):
        self.list = [(x + 1) for x in range(19)]
        random.shuffle(self.list)
        self.step = 1

        window = Tk()
        window.title("Selection Sort Animation")

        self.canvas = Canvas(window, width=600, height=500)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        Button(frame, text="step", command=self.fun).pack(side=LEFT)
        Button(frame, text="reset", command=self.reset).pack(side=LEFT)

        self.drawHistogram()
        window.mainloop()

    def fun(self):
        if self.step == 20:
            return
        arg = 0
        for i in range(len(self.list)):
            if self.list[i] == self.step:
                arg = i
        temp = self.list[self.step - 1]
        self.list[self.step - 1] = self.list[arg]
        self.list[arg] = temp

        self.canvas.delete("Histogram")
        self.drawHistogram()
        self.canvas.create_rectangle(80 + self.step * 20, 420, 100 + self.step * 20, 420 - self.step * 20,
                                     fill="black", tags="Histogram")
        self.step += 1

    def reset(self):
        try:
            self.step = 1
            random.shuffle(self.list)
            self.canvas.delete("Histogram")
        except TclError:
            pass
        self.drawHistogram()

    def drawHistogram(self):
        x = 100
        y = 420
        for i in range(19):
            h = self.list[i]
            self.canvas.create_rectangle(
                x, y, x + 20, y - h * 20, tags="Histogram")
            self.canvas.create_text(
                x + 5,
                y - h * 20 - 10,
                text=str(h),
                tags="Histogram")
            x += 20


if __name__ == '__main__':
    SelectSort()
