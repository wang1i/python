from tkinter import *
import time


class RaceCar:
    def __init__(self):
        window = Tk()
        window.title("Race Car")

        self.canvas = Canvas(window, width=800, height=500)
        self.canvas.pack()

        self.x = 0
        self.y = 450
        try:
            while True:
                self.x += 50
                if self.x == 700:
                    self.x = 0
                self.draw_car()
                window.update()
                time.sleep(0.2)
                self.canvas.delete("car")
        except TclError:
            pass


        window.mainloop()

    def draw_car(self):
        self.canvas.create_polygon(self.x + 10, self.y - 20, self.x + 20, self.y - 30,
                                   self.x + 30, self.y - 30, self.x + 40, self.y - 20,
                                   fill="brown", tags="car")
        self.canvas.create_rectangle(self.x, self.y - 20, self.x + 50, self.y - 10,
                                     fill="green", tags="car")
        self.canvas.create_text(self.x + 25, self.y - 15, text = "wl+", fill = "white",tags = "car")
        self.canvas.create_oval(self.x + 10, self.y - 10, self.x + 20, self.y,
                                fill="black", tags="car")
        self.canvas.create_oval(self.x + 30, self.y - 10, self.x + 40, self.y,
                                fill="black", tags="car")

RaceCar()