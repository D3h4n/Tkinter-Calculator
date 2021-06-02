from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Images')
root.iconbitmap('calculator.ico')

my_img = ImageTk.PhotoImage(Image.open("download.png"))
my_label = Label(image=my_img)
my_label.pack()

my_button = Button(root, text="terminate program", command=root.quit)
my_button.pack()
root.mainloop()