from tkinter import *


class ArrowKeys:
    def __init__(self):
        self.x = 200
        self.y = 150

        window = Tk()
        window.title("Arrow Keys")

        self.canvas = Canvas(window, width=400, height=300)
        self.canvas.pack()
        self.canvas.bind("<Up>", self.go_up)
        self.canvas.focus_set()
        self.canvas.bind("<Down>", self.go_down)
        self.canvas.focus_set()
        self.canvas.bind("<Left>", self.go_left)
        self.canvas.focus_set()
        self.canvas.bind("<Right>", self.go_right)
        self.canvas.focus_set()

        window.mainloop()

    def go_up(self,event):
        y_t = self.y - 20
        x_t = self.x
        self.canvas.create_line(self.x, self.y, x_t, y_t, tags="line")
        self.x = x_t
        self.y = y_t

    def go_down(self, event):
        y_t = self.y + 20
        x_t = self.x
        self.canvas.create_line(self.x, self.y, x_t, y_t, tags="line")
        self.x = x_t
        self.y = y_t

    def go_left(self, event):
        x_t = self.x - 20
        y_t = self.y
        self.canvas.create_line(self.x, self.y, x_t, y_t, tags="line")
        self.x = x_t
        self.y = y_t

    def go_right(self, event):
        x_t = self.x + 20
        y_t = self.y
        self.canvas.create_line(self.x, self.y, x_t, y_t, tags="line")
        self.x = x_t
        self.y = y_t


ArrowKeys()
