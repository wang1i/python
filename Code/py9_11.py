from tkinter import *
import time
import math


class DrawClock:

    def __init__(self):
        window = Tk()
        window.title("Draw Clock")

        self.canvas = Canvas(window, width=600, height=600)
        self.canvas.pack()
        self.canvas.create_oval(50, 50, 350, 350)
        self.points()
        try:
            while True:
                tm = time.localtime()
                t = time.asctime(tm)
                if tm.tm_hour <= 12:
                    t_hour = tm.tm_hour
                else:
                    t_hour = tm.tm_hour - 12
                rad1 = 2 * math.pi * (t_hour + tm.tm_min / 60) / 12
                rad2 = 2 * math.pi * (tm.tm_min + tm.tm_sec / 60) / 60
                rad3 = 2 * math.pi * tm.tm_sec / 60
                self.createline(50, 6, rad1)
                self.createline(90, 3, rad2)
                self.createline(120, 1, rad3)

                self.canvas.create_text(170, 450, text=t, tags="text")
                window.update()
                time.sleep(1)
                self.canvas.delete("line")
                self.canvas.delete("text")
                window.update()
        except TclError:
            pass
        window.mainloop()

    def points(self):
        for i in range(1, 13):
            x = 200 + 130 * math.sin(2 * math.pi * i / 12)
            y = 200 - 130 * math.cos(2 * math.pi * i / 12)
            self.canvas.create_text(x, y, text=str(i))

    def createline(self, radius, line_width, rad):
        x = 200 + radius * math.sin(rad)
        y = 200 - radius * math.cos(rad)
        self.canvas.create_line(200, 200, x, y, width=line_width, tags="line")


DrawClock()
