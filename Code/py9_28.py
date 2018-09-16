from tkinter import *
import math
import random as r


class DisplayTriAngle:
    def __init__(self):
        window = Tk()
        window.title("Triangle angle")

        self.canvas = Canvas(window, width = 600, height = 400)
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.movePoint)
        self.p1 = Point()
        self.p2 = Point()
        self.p3 = Point()

        self.draw_triangle()

        window.mainloop()

    def draw_triangle(self):
        self.canvas.create_polygon(self.p1.getX(), self.p1.getY(), self.p2.getX(), self.p2.getY(),
                                   self.p3.getX(), self.p3.getY(), fill = "red", tags = "tri")
        e1 = math.sqrt((self.p2.getX() - self.p3.getX()) ** 2 + (self.p2.getY() - self.p3.getY()) ** 2)
        e2 = math.sqrt((self.p1.getX() - self.p3.getX()) ** 2 + (self.p1.getY() - self.p3.getY()) ** 2)
        e3 = math.sqrt((self.p2.getX() - self.p1.getX()) ** 2 + (self.p2.getY() - self.p1.getY()) ** 2)

        A1 = math.degrees(math.acos((e1 ** 2 - e2 ** 2 - e3 ** 2) / (-2 * e2 * e3)))
        A2 = math.degrees(math.acos((e2 ** 2 - e1 ** 2 - e3 ** 2) / (-2 * e1 * e3)))
        A3 = math.degrees(math.acos((e3 ** 2 - e2 ** 2 - e1 ** 2) / (-2 * e1 * e2)))

        self.p1.setAngle(A1)
        self.p2.setAngle(A2)
        self.p3.setAngle(A3)

        self.canvas.create_text(self.p1.getX(), self.p1.getY(), text = str(int(A1)), tags = "tri")
        self.canvas.create_text(self.p2.getX(), self.p2.getY(), text = str(int(A2)), tags = "tri")
        self.canvas.create_text(self.p3.getX(), self.p3.getY(), text = str(int(A3)), tags = "tri")

    def movePoint(self, event):
        try:
            self.canvas.delete("tri")
        except TclError:
            pass
        d1 = math.sqrt((event.x - self.p1.getX()) ** 2 + (event.y - self.p1.getY()) ** 2)
        d2 = math.sqrt((event.x - self.p2.getX()) ** 2 + (event.y - self.p2.getY()) ** 2)
        d3 = math.sqrt((event.x - self.p3.getX()) ** 2 + (event.y - self.p3.getY()) ** 2)

        if d1 == min(d1, d2, d3):
            self.p1.setX(event.x)
            self.p1.setY(event.y)
        elif d2 == min(d1, d2, d3):
            self.p2.setX(event.x)
            self.p2.setY(event.y)
        else:
            self.p3.setX(event.x)
            self.p3.setY(event.y)

        self.draw_triangle()


class Point:
    def __init__(self):
        self.__x = r.random() * 590
        self.__y = r.random() * 390
        self.__angle = 0

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

    def setAngle(self, angle):
        self.__angle = angle


DisplayTriAngle()




