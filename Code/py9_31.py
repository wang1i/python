from tkinter import *


class DisplayFilledCircle:
    def __init__(self):
        window = Tk()
        window.title("Drogging the blue circle")

        self.canvas = Canvas(window, width = 600, height = 400)
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.moveBlue)

        self.canvas.create_oval(100, 100, 200, 200, fill = "blue", tags = "blue")
        self.canvas.create_oval(220, 100, 320, 200, fill = "black", tags = "rest")
        self.canvas.create_oval(340, 100, 440, 200, fill = "brown", tags = "rest")
        self.canvas.create_oval(160, 150, 260, 250, fill = "white", tags = "rest")
        self.canvas.create_oval(290, 150, 390, 250, fill = "gray", tags = "rest")

        window.mainloop()

    def moveBlue(self, event):
        try:
            self.canvas.delete("blue")
        except TclError:
            pass
        self.canvas.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50,
                                fill = "blue", tags = "blue")


DisplayFilledCircle()