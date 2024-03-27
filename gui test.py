from tkinter import *

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self)
        
        self.b1 = Button(parent, text = "bye bye", command = self.quit)
        self.b1.pack()

        self.b2 = Button(parent, text = "Hype", command = self.say)
        self.b2.pack()
    
    def say():
        pass
    
    def quit():
        pass

    
window = Tk()
window.title("Test Window")
# app = App(window)

# l1 = Label(window, bg = "yellow")
# l1.pack(side = LEFT, expand = 1, fill = BOTH)
# l2 = Label(window, bg = "red")
# l2.pack(side = LEFT, expand = 1, fill = BOTH)
# l3 = Label(window, bg = "blue")
# l3.pack(side = LEFT, expand = 1, fill = BOTH)

l4 = Label(window, text = "oh no...")
l4.grid(row = 0, column = 0)
l5 = Label(window, text = "anyway")
l5.grid(row = 1, column = 0)

e1 = Entry(window, width = 15)
e1.grid(row = 0, column = 1)

e2 = Entry(window, width = 15)
e2.grid(row = 1, column = 1)





window.mainloop()
# l1 = Label(window, text = "Among Us")

# l1.mainloop()

