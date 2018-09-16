from tkinter import *
import math


class Pendulum:
    def __init__(self):
        window = Tk()
        window.title("Pendulum")

        self.canvas = Canvas(window, width = 500, height = 500)
        self.canvas.pack()
        self.canvas.create_text(50, 50, text = "Up加速\nDown减速\nS键停止\nR键重新开始",tags = "text")

        self.canvas.bind("<Up>", self.accelerate)
        self.canvas.bind("<Down>", self.decelerate)
        self.canvas.bind("<S>", self.stop)
        self.canvas.bind("<R>", self.restart)
        self.canvas.focus_set()

        self.rad = math.pi * 1 / 3
        self.sign = 1
        self.x = 0
        self.y = 0
        self.sleepTime = 200
        self.isStopped = False
        self.animate()

        window.mainloop()

    def accelerate(self, event):
        self.sleepTime -= 50

    def decelerate(self, event):
        self.sleepTime += 50

    def stop(self, event):
        self.isStopped = True

    def restart(self, event):
        self.isStopped = False
        self.animate()

    def draw_clock(self):
        self.canvas.create_oval(247, 20, 253, 26, fill="black", tags="clock")
        self.canvas.create_line(250, 23, self.x, self.y, tags="clock")
        self.canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20,
                                fill="black", tags = "clock")

    def animate(self):
        self.rad = math.pi / 3
        while not self.isStopped:
            if self.rad > math.pi * 2 / 3:
                self.sign = -1
            if self.rad < math.pi * 1 / 3:
                self.sign = 1
            try:
                self.x = 250 - 400 * math.cos(self.rad)
                self.y = 20 + 400 * math.sin(self.rad)
                self.draw_clock()
                self.canvas.update()
                self.canvas.after(self.sleepTime)
                self.rad += self.sign * math.pi / 18
                self.canvas.delete("clock")
            except TclError:
                pass
        if self.isStopped:
            self.draw_clock()
            self.canvas.update()


Pendulum()