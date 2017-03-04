print ("Type your name")
name = input()
count = 0
while (name != "your name"):
    print("Type your name")
    name = input()
    count = count + 1
    if (count == 3):
        break;
print ("thank you!")
