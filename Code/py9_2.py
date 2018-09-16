from tkinter import *

class Investment:
    def __init__(self):
        window = Tk()
        window.title("Investment Calculator")

        Label(window, text="投资金额").grid(row=1, column=1, sticky=W)
        Label(window, text="年数").grid(row=2, column=1, sticky=W)
        Label(window, text="年利率").grid(row=3, column=1, sticky=W)
        Label(window, text="总金额").grid(row=4, column=1, sticky=W)

        self.v1 = StringVar()
        Entry(window, textvariable = self.v1, justify = RIGHT).grid(row = 1, column = 2)
        self.v2 = StringVar()
        Entry(window, textvariable=self.v2, justify=RIGHT).grid(row=2, column=2)
        self.v3 = StringVar()
        Entry(window, textvariable=self.v3, justify=RIGHT).grid(row=3, column=2)

        Button(window, text = "计算", \
               command = self.calculate ).grid(row = 5, column = 2)
        self.v4 = StringVar()
        Label(window, textvariable = self.v4, justify = RIGHT).grid(row = 4, column = 2)

        window.mainloop()

    def calculate(self):
        self.v4.set(eval(self.v1.get()) * (1 + eval(self.v3.get()) / 1200)**(eval(self.v2.get()) * 12) )

Investment()