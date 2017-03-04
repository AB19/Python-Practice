StrVar = input ()
ListVar = StrVar.split (" ")

for i in range (len (ListVar) - 1):
    TempList = ListVar [i]
    print (TempList [0])
    print (TempList [0].upper())
    print (TempList)
    ListVar [i] = TempList

print (ListVar)
