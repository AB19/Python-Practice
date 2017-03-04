from tkinter import *

root = Tk()
# creates an empty window
topFrame = Frame (root)
topFrame.pack(side = TOP)
# creates a top frame

bottomFrame = Frame (root)
bottomFrame.pack (side = BOTTOM)
#creates a bottom frame

Button1 = Button (topFrame, text = "Submit", fg = "blue" , bg = "pink")
Button1.pack (side = LEFT)
# fg is optional
Button2 = Button (topFrame, text = "Cancel", fg = "red")
Button2.pack (side = RIGHT)

Button3 = Button (bottomFrame, text = "close", fg = "green")
Button3.pack ()


root.mainloop()
