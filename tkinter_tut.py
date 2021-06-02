from tkinter import *

root = Tk()

# Creating Labels
# myLabel = Label(root,text="Hello World!")
# myLabel2 = Label(root,text="My Name is Person")

# putting them on the screen
# myLabel.grid(row=0,column=0)
# myLabel2.grid(row=1,column=0)

# Buttons
# def click():
#     myLabel = Label(root, text="Clicked the button")
#     myLabel.pack()

# myButton = Button(root, text="Enter Name", command=click, fg="blue", bg="red")
# myButton.pack()

# Entry widget
e = Entry(root, width=50)
e.pack()
e.insert(0, "Name")

def click():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello, fg="black")
    myLabel.pack()

myButton = Button(root, text="Enter Name", command=click, fg="blue", bg="red")
myButton.pack()

root.mainloop()