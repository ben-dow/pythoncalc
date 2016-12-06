from tkinter import *

class App:
    def __init__(self,master):
        '''
        Initializes the Calculator Window
        '''
        frame = Frame(master,height=250,width=200)
        frame.pack_propagate(0)
        frame.pack()

        '''
        Initilaze Display Frame
        '''
        display_frame = Frame(frame)
        display_frame.pack()

        '''
        Calcualtions Display
        '''
        self.display = Text(display_frame,width=14,height=2)
        self.display.config(state=DISABLED)
        self.display.tag_configure('tag-right', justify='right')
        self.display.grid(row=0, column = 1, sticky=E+W)

        '''
        Initialize Button Frame
        '''
        button_frame = Frame(frame)
        button_frame.pack()

        '''
        Buttons
        '''
        self.numbers = list()
        for i in range(10):
            self.numbers.append(Button(
                button_frame,
                text= i,
                fg ="red",
                height=2,
                width=4,
                command = lambda i=i: self.display_append(i)
                ))
        for i in range(len(self.numbers)):
            if i == 0:
                self.numbers[i].grid(row = 4, column = 0,)
            elif i == 1:
                self.numbers[i].grid(row = 3, column = 0)
            elif i == 2:
                self.numbers[i].grid(row = 3, column = 1)
            elif i == 3:
                self.numbers[i].grid(row = 3, column = 2)
            elif i == 4:
                self.numbers[i].grid(row = 2, column = 0)
            elif i == 5:
                self.numbers[i].grid(row = 2, column = 1)
            elif i == 6:
                self.numbers[i].grid(row = 2, column = 2)
            elif i == 7:
                self.numbers[i].grid(row = 1, column = 0)
            elif i == 8:
                self.numbers[i].grid(row = 1, column = 1)
            elif i == 9:
                self.numbers[i].grid(row = 1, column = 2)

        '''
        Create Operation Buttons
        '''
        self.addition = Button(
            button_frame,
            fg ="red",
            text= '+',
            height=2,
            width=4,
            command = lambda i=i: self.display_append('+')
            )
        self.addition.grid(row = 1, column=3)

        self.subtract = Button(
            button_frame,
            fg ="red",
            text = '-',
            height=2,
            width=4,
            command = lambda i=i: self.display_append('-')
            )
        self.subtract.grid(row = 2, column=3)

        self.multiply = Button(
            button_frame,
            fg ="red",
            text= "*",
            height=2,
            width=4,
            command = lambda i=i: self.display_append('*')
            )
        self.multiply.grid(row = 3, column=3)

        self.divide = Button(
            button_frame,
            fg ="red",
            text= "/",
            height=2,
            width=4,
            command = lambda i=i: self.display_append('/')
            )
        self.divide.grid(row = 4, column=3)

        self.decimal =  Button(
            button_frame,
            fg ="red",
            text= ".",
            height=2,
            width=4,
            command = lambda i=i: self.display_append('.')
            )
        self.decimal.grid(row = 4, column=1)

        self.delete = Button(
            button_frame,
            fg ="red",
            text= "Del",
            height=2,
            width=4,
            command = self.display_backspace
            )
        self.delete.grid(row = 0, column=3)

        self.open_parenth = Button(
            button_frame,
            fg ="red",
            text= "(",
            height=2,
            width=4,
            command = lambda i=i: self.display_append('(')
            )
        self.open_parenth.grid(row = 0, column=0)

        self.close_parenth = Button(
            button_frame,
            fg ="red",
            text= ")",
            height=2,
            width=4,
            command = lambda: self.display_append(')')
            )
        self.close_parenth.grid(row = 0, column=1)

        self.exponent = Button(
            button_frame,
            fg ="red",
            text= "x^y",
            height=2,
            width=4,
            command = lambda: self.display_append('^')
            )
        self.exponent.grid(row = 0, column=2)

        self.compute = Button(
            display_frame, #The Display Frame Container --- NOT THE SAME CONTAINER AS THE OTHER OPERATIONS
            fg ="red",
            text= "=",
            height=2,
            width=4,
            )
        self.compute.grid(row = 0, column=2)

        self.clear = Button(
            button_frame,
            fg ="red",
            text= "Clr",
            height=2,
            width=4,
            command = lambda: self.display_clear()
            )
        self.clear.grid(row = 4, column=2)



    def display_append(self, value):
        self.display.config(state=NORMAL)
        self.display.insert(END,value,'tag-right')
        self.display.config(state=DISABLED)
    def display_backspace(self):
        self.display.config(state=NORMAL)
        self.display.delete(END)
        self.display.config(state=DISABLED)
    def display_clear(self):
        self.display.config(state=NORMAL)
        self.display.delete(1.0,END)
        self.display.config(state=DISABLED)
    def display_change(self):
        pass


root = Tk()
app = App(root)
root.title("Calculator")
root.mainloop()
