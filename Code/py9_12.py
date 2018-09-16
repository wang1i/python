from tkinter import *


class RotatingMessage:
    def __init__(self):
        window = Tk()
        window.title("Rotating Message")

        self.one = True
        self.canvas = Canvas(window, width=400, height=300)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.display)

        window.mainloop()

    def display(self, event):
        try:
            self.canvas.delete("msg")
        except TclError:
            pass
        if self.one:
            self.canvas.create_text(
                200, 150, text="Programming is fun", tags="msg")
        else:
            self.canvas.create_text(
                200, 150, text="It is fun to Program", tags="msg")
        self.one = bool(int(self.one) - 1)


RotatingMessage()
