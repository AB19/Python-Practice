NumOfStudents = int (input ())
StuList = []
for i in range (NumOfStudents + 1):
    StrVar = input ()
    TempList = StrVar.split (" ")
    StuList = StuList + TempList

LenList = len (StuList)
for i in range (LenList):
    if (StuList [i] is StuList [LenList - 1]):
        Average = (int (StuList [i + 1]) + int (StuList [i + 2]) + int (StuList [i + 3]) ) / 3
        print (Average)
