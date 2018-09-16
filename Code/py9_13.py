from tkinter import *


class MousePosition:
    def __init__(self):
        window = Tk()
        window.title("Mouse Position")

        self.turn = True
        self.canvas = Canvas(window, width=400, height=300)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.showPosition)

        window.mainloop()

    def showPosition(self, event):
        try:
            self.canvas.delete("text")
        except TclError:
            pass

        self.canvas.create_text(event.x, event.y,
                                text="(" + str(event.x_root) + "," + str(event.y_root) + ")", tags="text")




MousePosition()