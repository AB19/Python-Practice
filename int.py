strin = int (input ())


def  countSteps(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n == 2):
        return 2
    elif (n == 3):
        return 4
    else:
        y = 0
        for i in range (1, 4, 1):
            x = countSteps (n - i)
            y = y + x
            return y 

xx = countSteps (strin)
print (xx)
