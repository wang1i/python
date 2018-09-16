from tkinter import *


class Radios:
    def __init__(self):
        window = Tk()
        window.title("Radio Button and Buttons")

        frame1 = Frame(window)
        frame1.pack()
        self.v = IntVar()
        Radiobutton(frame1, text="Red", variable=self.v,
                    value=1, command=self.change_color).pack(side=LEFT)
        Radiobutton(frame1, text="Yellow", variable=self.v,
                    value=2, command=self.change_color).pack(side=LEFT)
        Radiobutton(frame1, text="White", variable=self.v,
                    value=3, command=self.change_color).pack(side=LEFT)
        Radiobutton(frame1, text="Gray", variable=self.v,
                    value=4, command=self.change_color).pack(side=LEFT)
        Radiobutton(frame1, text="Green", variable=self.v,
                    value=5, command=self.change_color).pack(side=LEFT)

        frame2 = Frame(window)
        frame2.pack()
        self.canvas = Canvas(frame2, width=400, height=200)
        self.canvas.pack()
        self.canvas.create_text(150, 80, text="Welcome", tags="text")
        self.dx = 10
        self.x = 150

        frame3 = Frame(window)
        frame3.pack()
        Button(frame3, text="<=", command=self.decelerate).pack(side = LEFT)
        Button(frame3, text=">=", command=self.accelerate).pack(side = LEFT)

        window.mainloop()

    def change_color(self):
        try:
            self.canvas.delete("text")
            if self.v.get() == 1:
                self.canvas.create_text(
                    150, 80, text="Welcome", fill="red", tags="text")
            elif self.v.get() == 2:
                self.canvas.create_text(
                    150, 80, text="Welcome", fill="yellow", tags="text")
            elif self.v.get() == 3:
                self.canvas.create_text(
                    150, 80, text="Welcome", fill="white", tags="text")
            elif self.v.get() == 4:
                self.canvas.create_text(
                    150, 80, text="Welcome", fill="gray", tags="text")
            else:
                self.canvas.create_text(
                    150, 80, text="Welcome", fill="green", tags="text")
        except TclError:
            pass

    def accelerate(self):
        try:
            while True:
                self.canvas.move("text", self.dx, 0)
                self.canvas.after(100)
                self.canvas.update()
                if self.x < 400:
                    self.x += self.dx
                else:
                    self.x = 0
                    self.canvas.delete("text")
                    self.canvas.create_text(
                        self.x, 80, text="Welcome", tags="text")
        except TclError:
            pass

    def decelerate(self):
        try:
            while True:
                self.canvas.move("text", -self.dx, 0)
                self.canvas.after(100)
                self.canvas.update()
                if self.x > 0:
                    self.x -= self.dx
                else:
                    self.x = 300
                    self.canvas.delete("text")
                    self.canvas.create_text(
                        self.x, 80, text="Welcome", tags="text")
        except TclError:
            pass


Radios()
