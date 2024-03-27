from tkinter import *

class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.setupLayout()
        self.shouldClear = True

    def setupLayout(self):
        #create a label for the display text
        self.display = Label(self, text = "hello :)", 
                             anchor = E, bg = "white",
                             height = 1, width = 15,
                             font = ("Arial", 50))
        #shove the label into the grid manager
        self.display.grid(row = 0, column = 0, columnspan = 4, sticky = E + N + W + S)
        self.pack()

        img = PhotoImage(file ="images/7.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("7"))
        # button = Button(self, bg = "white", text = "7", command = lambda:self.press7())
        button.image = img
        button.grid(row = 2, column = 0, sticky = N+S+W+E)


        img = PhotoImage(file ="images/8.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("8"))
        # button = Button(self, bg = "white", text = "8", command = lambda:self.press7())
        button.image = img
        button.grid(row = 2, column = 1, sticky = N+S+W+E)

        img = PhotoImage(file ="images/9.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("9"))
        # button = Button(self, bg = "white", text = "9", command = lambda:self.press7())
        button.image = img
        button.grid(row = 2, column = 2, sticky = N+S+W+E)

        img = PhotoImage(file ="images/div.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("/"))
        # button = Button(self, bg = "white", text = "/", command = lambda:self.press7())
        button.image = img
        button.grid(row = 2, column = 3, sticky = N+S+W+E)

        img = PhotoImage(file ="images/4.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("4"))
        # button = Button(self, bg = "white", text = "4", command = lambda:self.press7())
        button.image = img
        button.grid(row = 3, column = 0, sticky = N+S+W+E)

        img = PhotoImage(file ="images/5.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("5"))
        # button = Button(self, bg = "white", text = "5", command = lambda:self.press7())
        button.image = img
        button.grid(row = 3, column = 1, sticky = N+S+W+E)

        img = PhotoImage(file ="images/6.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("6"))
        # button = Button(self, bg = "white", text = "6", command = lambda:self.press7())
        button.image = img
        button.grid(row = 3, column = 2, sticky = N+S+W+E)

        img = PhotoImage(file ="images/mul.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("*"))
        # button = Button(self, bg = "white", text = "*", command = lambda:self.press7())
        button.image = img
        button.grid(row = 3, column = 3, sticky = N+S+W+E)

        img = PhotoImage(file ="images/1.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("1"))
        # button = Button(self, bg = "white", text = "1", command = lambda:self.press7())
        button.image = img
        button.grid(row = 4, column = 0, sticky = N+S+W+E)

        img = PhotoImage(file ="images/2.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("2"))
        # button = Button(self, bg = "white", text = "2", command = lambda:self.press7())
        button.image = img
        button.grid(row = 4, column = 1, sticky = N+S+W+E)

        img = PhotoImage(file ="images/3.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("3"))
        # button = Button(self, bg = "white", text = "3", command = lambda:self.press7())
        button.image = img
        button.grid(row = 4, column = 2, sticky = N+S+W+E)

        img = PhotoImage(file ="images/sub.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("-"))
        # button = Button(self, bg = "white", text = "-", command = lambda:self.press7())
        button.image = img
        button.grid(row = 4, column = 3, sticky = N+S+W+E)

        img = PhotoImage(file ="images/0.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("0"))
        # button = Button(self, bg = "white", text = "0", command = lambda:self.press7())
        button.image = img
        button.grid(row = 5, column = 0, sticky = N+S+W+E)

        img = PhotoImage(file ="images/dot.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("."))
        # button = Button(self, bg = "white", text = ".", command = lambda:self.press7())
        button.image = img
        button.grid(row = 5, column = 1, sticky = N+S+W+E)

        img = PhotoImage(file ="images/add.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("+"))
        # button = Button(self, bg = "white", text = "+", command = lambda:self.press7())
        button.image = img
        button.grid(row = 5, column = 3, sticky = N+S+W+E)

        img = PhotoImage(file ="images/lpr.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("("))
        # button = Button(self, bg = "white", text = "(", command = lambda:self.press7())
        button.image = img
        button.grid(row = 1, column = 0, sticky = N+S+W+E)

        img = PhotoImage(file ="images/rpr.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process(")"))
        # button = Button(self, bg = "white", text = ")", command = lambda:self.press7())
        button.image = img
        button.grid(row = 1, column = 1, sticky = N+S+W+E)

        img = PhotoImage(file ="images/clr.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("AC"))
        # button = Button(self, bg = "white", text = "AC", command = lambda:self.press7())
        button.image = img
        button.grid(row = 1, column = 2, sticky = N+S+W+E)

        img = PhotoImage(file ="images/bak.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("back"))
        # button = Button(self, bg = "white", text = "^", command = lambda:self.press7())
        button.image = img
        button.grid(row = 1, column = 3, sticky = N+S+W+E)

        img = PhotoImage(file ="images/mod.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("%"))
        # button = Button(self, bg = "white", text = "^", command = lambda:self.press7())
        button.image = img
        button.grid(row = 6, column = 3, sticky = N+S+W+E)

        img = PhotoImage(file ="images/pow.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("**"))
        # button = Button(self, bg = "white", text = "^", command = lambda:self.press7())
        button.image = img
        button.grid(row = 6, column = 2, sticky = N+S+W+E)

        img = PhotoImage(file ="images/eql-wide.gif")
        button = Button(self, bg = "white", image = img, command = lambda:self.process("="))
        # button = Button(self, bg = "white", text = "=", command = lambda:self.press7())
        button.image = img
        button.grid(row = 6, column = 0, columnspan = 2, sticky = N+S+W+E)


    def process(self, value):
        if (self.shouldClear):
            self.display["text"] = ""
            self.shouldClear = False

        if (value == "="):
            expr = self.display["text"]
            try:
                result = str(eval(expr))
            except:
                result = "ERROR"

            if (len(result) > 14):
                result = result[0:11] + "..."
            self.display["text"] = result
            self.shouldClear = True

        elif (value == "AC"):
            self.display["text"] = ""

        elif (value == "back"):
            self.display["text"]  = self.display["text"][:-1]

        else: 
            if (not len( self.display["text"]) >= 14):
                self.display["text"] += value



window = Tk()

c = Calculator(window)

window.mainloop()