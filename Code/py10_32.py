from tkinter import *


s1 = input("enter point one with x and y:").split()
s2 = input("enter point two with x and y:").split()


p1 = [eval(x) for x in s1]
p2 = [eval(x) for x in s2]

window = Tk()
window.title("draw a line")
canvas = Canvas(window, width = 400, height = 300)
canvas.pack()
canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="line")

window.mainloop()