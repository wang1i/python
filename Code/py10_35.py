from tkinter import *
import random


class BounceBalls:
    def __init__(self):
        self.ballList = []

        window = Tk()
        window.title("Bouncing Balls")

        self.width = 600
        self.height = 400
        self.canvas = Canvas(window, width = self.width, height = self.height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume", command = self.resume)
        btResume.pack(side = LEFT)
        btAdd = Button(frame, text = "+", command = self.add)
        btAdd.pack(side = LEFT)
        btSub = Button(frame, text = "-", command = self.sub)
        btSub.pack(side = LEFT)
        btFaster = Button(frame, text = "Faster", command = self.faster)
        btFaster.pack(side = LEFT)
        btSlower = Button(frame, text = "slower", command = self.slower)
        btSlower.pack(side = LEFT)

        self.sleepTime = 100
        self.isStopped = False
        self.animate()

        window.mainloop()

    def stop(self):
        self.isStopped = True

    def resume(self):
        self.isStopped = False
        self.animate()

    def add(self):
        self.ballList.append(Ball())

    def sub(self):
        self.ballList.pop()

    def faster(self):
        if self.sleepTime > 0:
            self.sleepTime -= 20

    def slower(self):
        self.sleepTime += 20

    def animate(self):
        while not self.isStopped:
            try:
                self.canvas.update()
                self.canvas.after(self.sleepTime)
                self.canvas.delete("ball")
            except TclError:
                pass
            for ball in self.ballList:
                self.displayBall(ball)

    def displayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx
        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy

        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - 5, ball.y - 5, ball.x + 5, ball.y + 5,
                                fill = ball.color, tags = "ball")



class Ball:
    def __init__(self):
        self.x = random.random() * 600
        self.y = random.random() * 400
        self.dx = 4
        self.dy = 4
        self.color = getRandomColor()

def getRandomColor():
    color = "#"
    for _ in range(6):
        rand = random.randint(0, 15)
        if 0 <= rand <= 9:
            ch = chr(rand + ord('0'))
        else:
            ch = chr(rand -10 + ord('A'))
        color += ch
    return color


if __name__ == '__main__':
    BounceBalls()