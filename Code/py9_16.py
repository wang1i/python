from tkinter import *
import time

class DynamicFan:
    def __init__(self):
        window = Tk()
        window.title("Dynmic Fan")

        self.canvas = Canvas(window, width = 400, height = 400)
        self.canvas.pack()
        i = 0
        try:
            while True:
                i += 10
                self.canvas.create_arc(50, 50, 350, 350, start=90 + i, extent=30, fill="yellow", tags="arc")
                self.canvas.create_arc(50, 50, 350, 350, start=180 + i, extent=30, fill="yellow", tags="arc")
                self.canvas.create_arc(50, 50, 350, 350, start=270 + i, extent=30, fill="yellow", tags="arc")
                self.canvas.create_arc(50, 50, 350, 350, start=0 + i, extent=30, fill="yellow", tags="arc")
                window.update()
                time.sleep(0.1)
                self.canvas.delete("arc")
        except TclError:
            pass
        window.mainloop()
DynamicFan()
