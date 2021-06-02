from tkinter import *
import math

root = Tk()
root.title('Calculator')
root.iconbitmap('calculator.ico')

# declarations
width = 40
height = 20
option = -1
skip = False

class Option():
    add = 1
    sub = 2
    mul = 3
    divide = 4

Options = Option()

# text box
e = Entry(root,width=35, borderwidth = 5)
e.grid(row=0,column=0,columnspan=4, padx=10, pady=5)
e.insert(0, "0")

# functions
def button_decimal():
    global skip

    current = e.get()

    if current == 0:
        skip = True

    e.delete(0, END)
    e.insert(0, current + ".")

def button_insert(number):
    global skip

    if not skip:
        e.delete(0, END)
        skip = True

    current = e.get()

    e.delete(0, END)
    e.insert(0, current + str(number))

def clear():
    global f_num, option, skip

    e.delete(0, END)

    f_num = 0.0

    e.insert(0, "0")

    option = -1

    skip = False

def button_add():
    global f_num, option, skip

    num1 = e.get()

    f_num = round(float(num1),4)

    option = Options.add

    skip = False

def button_sub():
    global f_num, option, skip

    num1 = e.get()

    f_num = round(float(num1),4)

    option = Options.sub

    skip = False

def button_mul():
    global f_num, option, skip

    num1 = e.get()

    f_num = round(float(num1),4)

    option = Options.mul

    skip = False

def button_div():
    global f_num, option, skip

    num1 = e.get()

    f_num = round(float(num1),4)

    option = Options.divide

    skip = False

def button_negate():
    num = round(float(e.get()),4)
    
    if num != 0:
        e.delete(0, END)
        e.insert(0, str(-num))

def equal():
    global f_num, option, skip
    num2 = round(float(e.get()),4)

    if option is Option.add:
        e.delete(0, END)
        e.insert(0, str(f_num + num2))

    elif option is Option.sub:
        e.delete(0, END)
        e.insert(0, str(f_num - num2))

    elif option is Option.mul:
        e.delete(0, END)
        e.insert(0, str(round(f_num * num2, 4)))
    
    elif option is Option.divide:
        if num2 != 0:
            e.delete(0, END)
            e.insert(0, str(round(f_num / num2, 4)))
        else:
            e.delete(0, END)
            e.insert(0, "Error")
    else:
        f_num = round(float(e.get()),4)
        e.delete(0, END)
        e.insert(0, str(f_num))


    f_num = 0.0
    option = 0
    skip = False


# define buttons
# numbers
button_1 = Button(root, text="  1  ", padx=width, pady=height, command=lambda: button_insert(1))
button_2 = Button(root, text="  2  ", padx=width, pady=height, command=lambda: button_insert(2))
button_3 = Button(root, text="  3  ", padx=width, pady=height, command=lambda: button_insert(3))

button_4 = Button(root, text="  4  ", padx=width, pady=height, command=lambda: button_insert(4))
button_5 = Button(root, text="  5  ", padx=width, pady=height, command=lambda: button_insert(5))
button_6 = Button(root, text="  6  ", padx=width, pady=height, command=lambda: button_insert(6))

button_7 = Button(root, text="  7  ", padx=width, pady=height, command=lambda: button_insert(7))
button_8 = Button(root, text="  8  ", padx=width, pady=height, command=lambda: button_insert(8))
button_9 = Button(root, text="  9  ", padx=width, pady=height, command=lambda: button_insert(9))

button_0 = Button(root, text="  0  ", padx=width, pady=height, command=lambda: button_insert(0))

# mathematical functions
button_add = Button(root, text="+", padx=width, pady=height, command=button_add)
button_subtract = Button(root, text="-", padx=width+1, pady=height, command=button_sub) 
button_multiply = Button(root, text="x", padx=width, pady=height, command=button_mul)
button_divide = Button(root, text="/", padx=width, pady=height, command=button_div)

# utility
button_decimal = Button(root, text="  .   ", padx=width, pady = height, command=button_decimal)
button_negate = Button(root, text="+/-", padx=width, pady = height, command=button_negate)
button_equal = Button(root, text=" =  ", padx=width, pady=height, bg="orange", command=equal)
button_clear = Button(root, text="c", padx=width, pady=height, bg="orange", command=clear)

# Put the buttons on the screen
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_0.grid(row=5,column=0)

button_add.grid(row=2,column=3)
button_subtract.grid(row=3,column=3)
button_multiply.grid(row=4,column=3)
button_divide.grid(row=5,column=3)

button_decimal.grid(row=5, column=1)
button_negate.grid(row=1,column=2)
button_equal.grid(row=5,column=2)
button_clear.grid(row=1,column=3)

#main loop
root.mainloop()