from tkinter import *


class TrafficLights:
    def __init__(self):
        window = Tk()
        window.title("Traffic Lights")

        self.canvas = Canvas(window, width = 400, height = 400)
        self.canvas.pack()
        self.canvas.create_rectangle(150, 50, 250, 350, tags = "rect")
        self.draw_oval()

        frame = Frame(window)
        frame.pack()
        self.v = IntVar()
        Radiobutton(frame, text = "Red", variable = self.v, value = 1, command = self.changeColor).pack(side = LEFT)
        Radiobutton(frame, text = "Yellow", variable = self.v, value = 2, command = self.changeColor).pack(side = LEFT)
        Radiobutton(frame, text = "Green", variable = self.v, value = 3, command = self.changeColor).pack(side = LEFT)

        window.mainloop()

    def draw_oval(self):
        self.canvas.create_oval(150, 50, 250, 150, tags = "oval")
        self.canvas.create_oval(150, 150, 250, 250, tags = "oval")
        self.canvas.create_oval(150, 250, 250, 350, tags = "oval")

    def changeColor(self):
        try:
            if self.v.get() == 1:
                self.canvas.delete("yellow")
                self.canvas.delete("green")
                self.draw_oval()
                self.canvas.create_oval(150, 50, 250, 150, fill = "red", tags = "red")
            if self.v.get() == 2:
                self.canvas.delete("red")
                self.canvas.delete("green")
                self.draw_oval()
                self.canvas.create_oval(150, 150, 250, 250, fill = "yellow", tags = "yellow")
            if self.v.get() == 3:
                self.canvas.delete("red")
                self.canvas.delete("yellow")
                self.draw_oval()
                self.canvas.create_oval(150, 250, 250, 350, fill = "green", tags = "green")
        except TclError:
            pass

TrafficLights()
