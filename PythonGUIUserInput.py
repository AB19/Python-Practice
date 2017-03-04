from tkinter import *

root = Tk()

label1 = Label (root, text = "Enter the location of the file along with its name: ", fg = "blue")
label1.grid (row = 0, column = 0)

Entry1 = Entry (root)
Entry1.grid (row = 0, column = 1)

print (Entry1)

root.mainloop()
