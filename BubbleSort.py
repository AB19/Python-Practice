UserInput = input ("Enter the values separated by spaces: \n")
MyList = UserInput.split (" ")
ListLen = len (MyList)

for i in range (0, ListLen - 1):
    for j in range (0, ListLen - 1 - i):
        if (int (MyList [j]) > int (MyList [j + 1])):
            MyList [j], MyList [j + 1] = MyList [j + 1], MyList [j]

print (MyList)
