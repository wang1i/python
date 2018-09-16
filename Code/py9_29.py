from tkinter import *
import math


class Intersecting:
    def __init__(self):
        window = Tk()
        window.title("Intersecting points")

        self.canvas = Canvas(window, width = 600, height = 400)
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.moveLine)

        self.p11 = Point(20, 20)
        self.p12 = Point(56, 130)
        self.p21 = Point(100, 20)
        self.p22 = Point(16, 130)

        self.drawLines()

        window.mainloop()

    def drawLines(self):
        try:
            self.canvas.delete("lines")
        except TclError:
            pass
        self.canvas.create_line(self.p11.getX(), self.p11.getY(),
                                self.p12.getX(), self.p12.getY(), tags = "lines")
        self.canvas.create_line(self.p21.getX(), self.p21.getY(),
                                self.p22.getX(), self.p22.getY(), tags = "lines")

    def moveLine(self, event):
        if self.distance(event.x, event.y, self.p11) < 20:
            self.p11.setX(event.x)
            self.p11.setY(event.y)
            self.drawLines()
        if self.distance(event.x, event.y, self.p12) < 20:
            self.p12.setX(event.x)
            self.p12.setY(event.y)
            self.drawLines()
        if self.distance(event.x, event.y, self.p21) < 20:
            self.p21.setX(event.x)
            self.p21.setY(event.y)
            self.drawLines()
        if self.distance(event.x, event.y, self.p22) < 20:
            self.p22.setX(event.x)
            self.p22.setY(event.y)
            self.drawLines()

    def distance(self, x, y, p):
        return math.sqrt((x - p.getX()) ** 2 + (y - p.getY()) ** 2)


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getAngle(self):
        return self.__angle

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y


Intersecting()