from tkinter import *

class drawGeometry:
    def __init__(self):
        window = Tk()
        window.title("画图")

        self.canvas = Canvas(window, bg = "white", width = 300, height = 200)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        self.v1 = IntVar()
        rectangle = Radiobutton(frame, text = "Rectangle", variable = self.v1, value = 1,
                                command = self.drawRectangle)
        rectangle.pack(side = LEFT)
        oval = Radiobutton(frame, text="Oval", variable=self.v1, value=2,
                                command=self.drawOval)
        oval.pack(side = LEFT)
        self.v2 = IntVar()
        filled = Checkbutton(frame, text = "Filled", variable = self.v2, command = self.draw1)
        filled.pack()

        window.mainloop()

    def drawRectangle(self):
        try:
            self.canvas.delete("rect")
            self.canvas.delete("oval")
        except TclError:
            pass
        if self.v1.get() == 1 and self.v2.get() == 1:
            self.canvas.create_rectangle(50, 150, 250, 20, fill="red", tags="rect")
        elif self.v1.get() == 1 and self.v2.get() == 0:
            self.canvas.create_rectangle(50, 150, 250, 20, tags="rect")

    def drawOval(self):
        try:
            self.canvas.delete("rect")
            self.canvas.delete("oval")
        except TclError:
            pass
        if self.v1.get() == 2 and self.v2.get() == 1:
            self.canvas.create_oval(50, 150, 250, 20, fill="red", tags="oval")
        elif self.v1.get() == 2 and self.v2.get() == 0:
            self.canvas.create_oval(50, 150, 250, 20, tags="oval")

    def draw1(self):
        try:
            self.canvas.delete("rect")
            self.canvas.delete("oval")
        except TclError:
            pass
        if self.v1.get() == 1 and self.v2.get() == 1:
            self.canvas.create_rectangle(50, 150, 250, 20, fill="red", tags="rect")
        elif self.v1.get() == 1 and self.v2.get() == 0:
            self.canvas.create_rectangle(50, 150, 250, 20, tags="rect")
        elif self.v1.get() == 2 and self.v2.get() == 1:
            self.canvas.create_oval(50, 150, 250, 20, fill="red", tags="oval")
        elif self.v1.get() == 2 and self.v2.get() == 0:
            self.canvas.create_oval(50, 150, 250, 20, tags="oval")

drawGeometry()


