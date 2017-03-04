# starting from the second value in the list, each value is checked
# against all the values to its left and placed at a suitable position.

UserInput = input ("Enter the elements separated by spaces:\n ")
MyList = UserInput.split (" ")
ListLen = len (MyList)

for i in range (1, ListLen): # from the first element to the last... upper limit - 1 in range function
    for j in range (i - 1, -1, -1):
        if (MyList [j] > MyList [j + 1]):
            MyList [j], MyList [j + 1] = MyList [j + 1], MyList [j]
        else:
            break

print (MyList)
