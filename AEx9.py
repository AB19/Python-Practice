# Guess my number Game

import random
MyNumber = random.randint(0,100)
#print (MyNumber)

print ("I have chosen a number betwwen 0 and 100 ")
print ("Enter your guess")
UserEntry = int(input())
count = 1
while (UserEntry != MyNumber):
    if (UserEntry > MyNumber):
        print ("Your guess " + str(UserEntry) + "is greater than my Number")
    elif (UserEntry < MyNumber):
        print ("Your guess " + str(UserEntry) + "is lesser than my Number")
    else:
        break;
    UserEntry = int(input())
    count = count + 1

print ("Congrats! you have guessed my number in " + str(count) + " guesses")
