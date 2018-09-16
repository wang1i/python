from tkinter import *
import math


class InTheCircle:
    def __init__(self):
        window = Tk()
        window.title("Inside the circle")

        self.canvas = Canvas(window, width=600, height=400)
        self.canvas.pack()
        self.canvas.create_oval(50, 10, 150, 110, tags="circle")
        self.canvas.bind("<B1-Motion>", self.in_circle)

        window.mainloop()

    def in_circle(self, event):
        distance = math.sqrt((event.x - 100)**2 + (event.y - 60)**2)
        try:
            self.canvas.delete("text")
        except TclError:
            pass
        if distance <= 50:
            self.canvas.create_text(event.x - 50, 60, text = "鼠标指针在圆内", tags="text")
        else:
            self.canvas.create_text(event.x - 50, 60, text = "鼠标指针不在圆内", tags="text")


InTheCircle()
