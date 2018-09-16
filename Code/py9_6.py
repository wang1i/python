from tkinter import *
import random

class XorO:
    def __init__(self):
        window = Tk()
        window.title("XOXO")

        xImage = PhotoImage(file = "C:\\Users\\Administrator\\Desktop\\262.gif")
        oImage = PhotoImage(file = "C:\\Users\\Administrator\\Desktop\\263.gif")

        for r in range(1, 4):
            for c in range(1, 4):
                if random.randint(0, 1) == 0:
                   Label(window, image = xImage).grid(row = r, column = c)
                else:
                    Label(window, image=oImage).grid(row=r, column=c)

        window.mainloop()

XorO()