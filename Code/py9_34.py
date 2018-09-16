from tkinter import *


class AddressBook:
    def __init__(self):
        window = Tk()
        window.title("AddressBook")
        self.list = []
        self.num = 0

        frame1 = Frame(window)
        frame1.grid(row = 1, column = 1)
        Label(frame1, text = "Name").grid(row = 1, column = 1)
        self.name = StringVar()
        Entry(frame1, textvariable = self.name, justify = LEFT).grid(row = 1, column = 2, sticky = W)
        Label(frame1, text="Street").grid(row = 2, column = 1)
        self.street = StringVar()
        Entry(frame1, textvariable = self.street, justify = LEFT).grid(row = 2, column = 2, sticky = W)
        Label(frame1, text="City").grid(row = 3, column = 1)
        self.city = StringVar()
        Entry(frame1, textvariable = self.city, justify = LEFT).grid(row = 3, column = 2)
        Label(frame1, text = "State").grid(row = 3, column = 3)
        self.state = StringVar()
        Entry(frame1, textvariable = self.state, justify = LEFT).grid(row = 3, column = 4)
        Label(frame1, text = "Zip").grid(row = 3, column = 5)
        self.zip = StringVar()
        Entry(frame1, textvariable = self.zip, justify = LEFT).grid(row = 3, column = 6)

        frame2 = Frame(window)
        frame2.grid(row = 2, column = 1, padx = 50)
        Button(frame2, text = "Add", command = self.add).grid(row = 1, column = 1)
        Button(frame2, text = "First", command = self.first).grid(row = 1, column = 2)
        Button(frame2, text = "Next", command = self.next).grid(row = 1, column = 3)
        Button(frame2, text = "Previous", command = self.previous).grid(row = 1, column = 4)
        Button(frame2, text = "Last", command = self.last).grid(row = 1, column = 5)

        window.mainloop()

    def add(self):
        self.list.append(Address(self.name.get(), self.street.get(), self.city.get(),
                                 self.state.get(), self.zip.get()))

    def first(self):
        self.list[0].getitem()

    def next(self):
        self.num += 1
        self.list[self.num].getitem()

    def previous(self):
        self.num -= 1
        self.list[self.num - 1].getitem()

    def last(self):
        self.list[-1].getitem()


class Address:
    def __init__(self, name, street, city, state, zip):
        self.__name = name
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip = zip

    def getitem(self):
        print("Name: " + self.__name + "\n" + "Street: " + self.__street + "\n" +
              "City: " + self.__city + "  State:" + self.__state + "  ZIP: " + self.__zip)

if __name__ == '__main__':
    AddressBook()

