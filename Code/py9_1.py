from tkinter import *

class MoveBall:
    def __init__(self):
        self.x1 = 300
        self.y1 = 200
        self.x2 = 320
        self.y2 = 220

        window = Tk()
        window.title("Moving Ball")

        self.canvas = Canvas(window, bg = "white", width = 600, height = 400)
        self.canvas.pack()
        self.radius = 50

        self.canvas.create_oval(300, 200, 320, 220, fill = "black", tags = "ball")


        frame = Frame(window)
        frame.pack()
        leftButton = Button(frame, text = "Left", bg = "white", command = self.Left)
        leftButton.pack(side = LEFT)
        rightButton = Button(frame, text = "Right", bg = "white", command = self.Right)
        rightButton.pack(side = LEFT)
        upButton = Button(frame, text = "Up", bg = "white", command = self.Up)
        upButton.pack(side = LEFT)
        downButton = Button(frame, text = "Down", bg = "white", command = self.Down)
        downButton.pack(side = LEFT)

        window.mainloop()

    def Left(self):
        try:
            self.canvas.delete("ball")
            self.x1 -= self.radius
            self.x2 -= self.radius
            if self.x1 < 0:
                return
            else:
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="black", tags="ball")
        except TclError:
            pass

    def Right(self):
        try:
            self.canvas.delete("ball")
            self.x1 += self.radius
            self.x2 += self.radius
            if self.x2 > 400:
                return
            else:
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="black", tags="ball")
        except TclError:
            pass

    def Up(self):
        try:
            self.canvas.delete("ball")
            self.y1 -= self.radius
            self.y2 -= self.radius
            if self.y2 < 0:
                return
            else:
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="black", tags="ball")
        except TclError:
            pass

    def Down(self):
        try:
            self.canvas.delete("ball")
            self.y1 += self.radius
            self.y2 += self.radius
            if self.y1 > 600:
                return
            else:
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="black", tags="ball")
        except TclError:
            pass

MoveBall()