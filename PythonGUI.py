# we have built in library the TKinter

from tkinter import *

root = Tk() # constructor of the tkinter class that creates a blank window
# this creates a window with the minimize, close and resize buttons. with the feather (tkinter) symbol
theLabel = Label(root, text = "Simple GUI")
theLabel2 = Label (root, text = "jaffa-Daffa")
# Label displays what you want to show to the user
theLabel.pack()
theLabel2.pack()
# says tkinter to pack the label wherever possible
root.mainloop() # computers are fast. so they open the window an close it very fast. mainloop puts in an infinite loop
#it keeps running.
