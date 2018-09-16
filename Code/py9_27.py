from tkinter import *


class ComputePayment:
    def __init__(self):
        window = Tk()
        window.title("Compare Interest Rates")

        frame1 = Frame(window)
        frame1.pack()
        frame2 = Frame(window)
        frame2.pack()

        Label(frame1, text = "Loan Amount").pack(side = LEFT)
        self.v1 = StringVar()
        Entry(frame1, width = 20, textvariable = self.v1, justify = RIGHT).pack(side = LEFT)
        Label(frame1, text="Years").pack(side=LEFT)
        self.v2 = StringVar()
        Entry(frame1, width=20, textvariable=self.v2, justify=RIGHT).pack(side=LEFT)
        Button(frame1, text = "Calculate", command = self.calculate).pack(side = LEFT)

        scrollbar = Scrollbar(frame2)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text = Text(frame2,wrap = WORD, yscrollcommand = scrollbar.set)
        self.text.pack()
        self.text.insert(END, "Interest Rates          Monthly Payment          Total Payment          ")
        scrollbar.config(command = self.text.yview)


        window.mainloop()

    def calculate(self):
        rate = 5.
        self.text.delete(2.0, 27.0)
        for _ in range(25):
            m_pay = eval(self.v1.get()) * rate / 1200 / (1 - 1 / (1 + rate / 1200)**(eval(self.v2.get()) * 12))
            t_pay = m_pay * eval(self.v1.get()) * 12
            self.text.insert(END,  "\n" + format(rate, "<24.2f") + format(m_pay , "<25.2f") + format(t_pay, "<23.2f") )
            rate += 0.125

ComputePayment()

