# detects all the email addresses..
# uses a findall () method to store the email addresses in a list.
import re
UserInput  = input ("Enter the Data: ")

def EmailFinder (UserInput):
    EmailRegex = re.compile (r"""(
    [a-zA-Z0-9._%+-]+ # lower, upper case, digits, . / % + -
    @
    [a-zA-Z0-9._%+-]+
    (\.[a-zA-Z]{2,4})
    )""", re.VERBOSE)

    EmailList = EmailRegex.findall (UserInput)
    print ("Email addresses found are: ")
    print ("\n", EmailList)

EmailFinder (UserInput)
