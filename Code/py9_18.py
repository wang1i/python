from tkinter import *

class FlashingText:
    def __init__(self):
        window = Tk()
        window.title("Flashing Text")

        self.canvas = Canvas(window, width = 600, height = 400)
        self.canvas.pack()

        try :
           while True:
               self.canvas.create_text(300, 200, text="Welcome", fill="red", tags="text")
               self.canvas.update()
               self.canvas.after(200)
               self.canvas.delete("text")
               self.canvas.update()
               self.canvas.after(200)
        except TclError:
            pass

        window.mainloop()

FlashingText()