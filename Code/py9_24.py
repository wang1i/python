from tkinter import *


class DynamicCircle:
    def __init__(self):
        window = Tk()
        window.title("Dynamic Circle")

        self.x = 270
        self.y = 270
        self.num = 0  #num表示画布上存在的圆的个数
        self.n = 0    #n表示总共画过的圆的个数
        self.list = []

        self.canvas = Canvas(window, width=600, height=600)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.add)
        self.canvas.bind("<Button-3>", self.reduce)

        window.mainloop()

    def add(self, event):
        if self.num == 0:
            self.x = 270
            self.y = 270
            self.num += 1
            self.n += 1
            self.list.append(self.n)
            self.canvas.create_oval(self.x, self.y, self.x + 60, self.y + 60, tags=str(self.n))
            print(self.list)
        else:
            self.x -= 20
            self.y -= 20
            self.num += 1
            self.n += 1
            self.list.append(self.n)
            self.canvas.create_oval(self.x, self.y, self.x + 60 + 2 * (self.num - 1) * 20,
                                    self.y + 60 + 2 * (self.num - 1) * 20, tags=str(self.n))
            print(self.list)

    def reduce(self, event):
        if self.num == 0:
            return
        else:
            try:
                self.canvas.delete(str(self.list[-1]))
                self.x += 20
                self.y += 20
            except TclError:
                pass
            self.num -= 1
            self.list = self.list[:-1]
        print(self.list)

DynamicCircle()

""" 注：这个程序中canvas.crate中的tags在经过创建删除后不能够再使用
    （如果再使用的话无法正确完成delete操作，只在这个程序中发现这问题），有洁癖？？不科学啊~~~
"""
