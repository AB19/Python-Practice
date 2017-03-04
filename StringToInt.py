# function to convert a string value to an integer

InputString = input ("Enter a Value: ")

def StringToInt (InputString):
    if (InputString = ''):
        return None
    else:
        return int (InputString)

IntValue = StringToInt (InputString)

# test case

print (IntValue + 222)
