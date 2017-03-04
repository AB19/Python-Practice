# Usage of maps
# general method
MyList = [1, 2, 3, 4, 5, 6]
Squared = []
Squared2 = []
Squared3 = []
for i in range (len (MyList)):
    Squared.append (MyList [i] ** 2)
print (Squared)
# using functions
def Square (x):
    return x ** 2
for i in range (len (MyList)):
    Squared2.append (Square (MyList [i]))
print (Squared2)
# using maps
Squared3 = list (map (Square, MyList))
print (Squared3)
