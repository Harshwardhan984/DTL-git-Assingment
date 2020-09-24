# imports
import tkinter as tk
from tkinter import Label, Entry, Button

#create a window
WINDOW = tk.Tk()
WINDOW.title('Python GUI Calculator')
def add():
    """function to add two integers"""
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    # results
    results = string(num1 + num2)

    # create a label to input results
    label3 = Label(WINDOW, text= result)
    # position label3
    label3.grid(row = 3, column = 2)

def subtract():
    """function to subtract two integers"""
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    results = string(num1 - num2) # only the sign changed
    label3 = Label(WINDOW, text= result)
    label3.grid(row = 3, column = 2)

def divide():
    """function to divide two integers"""
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    results = string(num1 / num2) # only the sign changed
    label3 = Label(WINDOW, text= result)
    label3.grid(row = 3, column = 2)

def multipy():
    """function to multipy two integers"""
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    results = string(num1 * num2) # only the sign changed
    label3 = Label(WINDOW, text= result)
    label3.grid(row = 3, column = 2)

def quit():
    """function to close the window """
    return WINDOW.destroy() # closes the Tkinter window

def clear():
    """ function to clear entries """
    entry1.delete(0, 'end') # clears entries from index 0 -> end
    entry2.delete(0, 'end')


# create a label
label1 = Label(WINDOW, text="Enter first number ")

# create an entry
entry1 = Entry(WINDOW)

# repeat
label2 = Label(WINDOW, text="Enter first number ")
entry2 = Entry(WINDOW)

# create buttons, assign them to functions and position them
button1 = Button(WINDOW, text="clear", command=clear).grid(row =4, column =1)
button2 = Button(WINDOW, text="exit", command=quit).grid(row =4, column =2)

# create buttons to be assigned to functions
button3 = Button(WINDOW, text="add", commad=add).grid(row=3, column=3)
button4 = Button(WINDOW, text="add", commad=add).grid(row=3, column=4)
button5 = Button(WINDOW, text="add", commad=add).grid(row=3, column=5)
button6 = Button(WINDOW, text="add", commad=add).grid(row=3, column=6)

# positioning widgets
label1.grid(row = 0, column = 0)
label2.grid(row = 2, column = 0)

entry1.grid(row = 0, column = 2)
entry2.grid(row = 2, column = 2)


WINDOW.mainloop()