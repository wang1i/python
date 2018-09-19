from tkinter import *


class ConsecutiveFour:
    def __init__(self):
        window = Tk()
        window.title("Consecutive Four")


        self.sd = []
        self.frame1 = Frame(window)
        self.frame1.grid(row = 1, column = 1)
        for i in range(6):
            self.sd.append([])
            for j in range(7):
                self.sd[i].append(StringVar())
                Entry(self.frame1, textvariable = self.sd[i][j],
                          justify = LEFT).grid(row = i + 1, column = j + 1)

        frame2 = Frame(window)
        frame2.grid(row = 2, column = 1)
        Button(frame2, text = "Solve", command = self.solve).grid(row = 1, column = 1, padx = 200)

        window.mainloop()

    def solve(self):
        for i in range(6):
            for j in range(7):
                if self.isValid(i, j)[0] == True:
                    if self.isValid(i, j)[1] == 1:
                        for k in range(j , j + 4):
                            Entry(self.frame1, textvariable = self.sd[i][k], bg = "gray").grid(row = i + 1, column = k + 1)
                    if self.isValid(i, j)[1] == 2:
                        for k in range(i, i + 4):
                            Entry(self.frame1, textvariable=self.sd[i][k], bg="gray").grid(row=i + 1, column = k)
                    if self.isValid(i, j)[1] == 3:
                        k = i
                        l = j
                        count = 0
                        while count < 4:
                            Entry(self.frame1, textvariable=self.sd[k][l], bg="gray").grid(row=k + 1, column=l + 1)
                            count += 1
                            k += 1
                            l += 1


    def isValid(self, i, j):
        k = i
        l = j
        if l <= 3 and eval(self.sd[k][l].get()) == eval(self.sd[k][l + 1].get()) \
                == eval(self.sd[k][l + 2].get()) == eval(self.sd[k][l + 3].get()):
            return [True, 1]
        if k <= 2 and eval(self.sd[k][l].get()) == eval(self.sd[k + 1][l].get()) \
                == eval(self.sd[k + 2][l].get()) == eval(self.sd[k + 3][l].get()):
            return [True, 2]
        if k <= 2 and l <= 3 and eval(self.sd[k][l].get()) == eval(self.sd[k + 1][l + 1].get()) \
                == eval(self.sd[k + 2][l + 2].get()) == eval(self.sd[k + 3][l + 3].get()):
            return [True, 3]
        return [False, 0]


if __name__ == '__main__':
    ConsecutiveFour()





