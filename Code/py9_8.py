from tkinter import *

class TriangleNumber:
    window = Tk()
    window.title("数字金字塔")

    for n in range(1, 12):
        s = ""
        for i in range(1, n):
            s += str(i) + " "
        s += str(n)
        Label(window, text = s).pack()

    window.mainloop()

TriangleNumber()