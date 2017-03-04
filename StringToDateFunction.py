# we need to import the 'datetime' class for this
from datetime import datetime

DateString = input ("Enter the date: ")

def StringToDate (DateString):
    if (DateString == ''):
        return None
    else:
        Date_Object = datetime.strptime (DateString, "%Y-%m-%d")
        return Date_Object

Date_Format = StringToDate (DateString)

print (Date_Format)
