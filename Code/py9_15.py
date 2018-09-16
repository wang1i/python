from tkinter import *

class StaticFan:
    def __init__(self):
        window = Tk()
        window.title("Static Fan")

        self.canvas = Canvas(window, width = 400, height = 400)
        self.canvas.pack()
        self.canvas.create_arc(50, 50, 350, 350, start=90, extent=30, fill="yellow", tags="arc")
        self.canvas.create_arc(50, 50, 350, 350, start=180, extent=30, fill="yellow", tags="arc")
        self.canvas.create_arc(50, 50, 350, 350, start=270, extent=30, fill="yellow", tags="arc")
        self.canvas.create_arc(50, 50, 350, 350, start=0, extent=30, fill="yellow", tags="arc")

        window.mainloop()

StaticFan()
