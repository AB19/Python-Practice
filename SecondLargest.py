ListLen = int (input ())
UserInput = input ()
MyList = UserInput.split (" ")

for i in range (1, ListLen): # from the first element to the last... upper limit - 1 in range function
    for j in range (i - 1, -1, -1):
        if (int (MyList [j]) > int (MyList [j + 1])):
            MyList [j], MyList [j + 1] = MyList [j + 1], MyList [j]
        else:
            break

for i in range (ListLen - 2, -1, -1):
    if (int (MyList [i]) < int (MyList [ListLen - 1])):
        print (MyList [i])
        break
