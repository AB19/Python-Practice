

UserInput = input()

def PhoneNumberFinder (x):
    import re
    PhoneNumberRegex = re.compile (r"\d\d\d-\d{3}-\d{4}")
    MatchObject = PhoneNumberRegex.search (x)
    print (MatchObject.group())

UserLength = len (UserInput)

for i in range (UserLength):
    x = UserInput [i : i + 12]
    print (x)
    PhoneNumberFinder (x)
