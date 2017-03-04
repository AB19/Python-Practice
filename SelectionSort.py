# loop through the list, find the least valued number, place it in the first placed
# second least, place it in second place and so on..


UserInput  = input ("Enter the values separated by space: \n")
MyList = UserInput.split (" ")
ListLen = len (MyList)

for i in range (0, ListLen - 1, 1):
    MinIndex = i
    for j in range (i + 1, ListLen):
        if (int (MyList [j]) < int (MyList [MinIndex])):
            MinIndex = j
    if (MinIndex != i):
        MyList [i], MyList [MinIndex] = MyList [MinIndex], MyList [i]

print (MyList)
