# using regexes
import re

def PhoneNumberFinder (StringVar):
    RegexObject = re.compile (r"\d{3}-\d{3}-\d{4}")
    MatchObject = RegexObject.findall (StringVar)
    print ("Phone Number: \n",  MatchObject)


UserInput = input ("Enter the text: \n")
PhoneNumberFinder (UserInput)
