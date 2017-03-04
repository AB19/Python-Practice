# find unique value in a given set of values

UserInput = input ("Enter a value: ")
UniqueList = []
while (UserInput != ''):
    if UserInput not in UniqueList:
        UniqueList.append (UserInput)
    UserInput = input()

print (UniqueList)

size = len (UniqueList)
print ("There are ", size, " unique entries.")
