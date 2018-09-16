from tkinter import *

class MovingCircle:
    def __init__(self):
        window = Tk()
        window.title("Moving Circle")

        self.x = 200
        self.y = 80

        self.canvas = Canvas(window, width = 600, height = 400)
        self.canvas.pack()
        self.canvas.create_oval(200, 80, 220, 100, tags = "oval")
        self.canvas.bind("<Up>", self.up)
        self.canvas.bind("<Down>", self.down)
        self.canvas.bind("<Left>", self.left)
        self.canvas.bind("<Right>", self.right)
        self.canvas.focus_set()

        window.mainloop()

    def up(self, event):
        try:
            self.canvas.delete("oval")
        except TclError:
            pass
        self.y -= 40
        self.canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20, tags = "oval")

    def down(self, event):
        try:
            self.canvas.delete("oval")
        except TclError:
            pass
        self.y += 40
        self.canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20, tags = "oval")

    def left(self, event):
        try:
            self.canvas.delete("oval")
        except TclError:
            pass
        self.x -= 40
        self.canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20, tags = "oval")

    def right(self, event):
        try:
            self.canvas.delete("oval")
        except TclError:
            pass
        self.x += 40
        self.canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20, tags = "oval")

MovingCircle()