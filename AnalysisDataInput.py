from tkinter import *


def evaluate(ss):
    Entry1.get()
    print (Entry1)

root = Tk()

Label1 = Label(root, text = "Enter the File Name along with its path: ") #add fg and bg here
Label1.grid(row = 0, column = 0)

Entry1 = Entry(root)
Entry1.grid(row = 0, column = 1)
Entry1.bind("<Return>", evaluate)

Label2 = Label(root)
Label2.grid(row = 2, column = 1)

Button1 = Button(root, text = "Submit")
Button1.grid(row = 3, column = 0)

Button2 = Button(root, text = "Cancel")
Button2.grid(row = 3, column = 1)

root.mainloop()
