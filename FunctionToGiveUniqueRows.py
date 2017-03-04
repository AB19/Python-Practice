import unicodecsv

print ("Enter the file name (along with the path if in different folder): ")
FileNameNPath = input ()

print ("Enter the primary key")
PrimaryKey = input ()

def FileToList (FileNameNPath):
    with open (FileNameNPath, 'rb') as FileObject:
        ReaderCsv = unicodecsv.DictReader (FileObject)
        return list (ReaderCsv)

def Display (ListToDisplay):
    size = len (ListToDisplay)
    print ("size of the list ", size)
    print (ListToDisplay[0][PrimaryKey])
    print (ListToDisplay[0])
    #for i in range (size):
    #    print (ListToDisplay[i])

def DisplayUnique (ListToDisplay, PrimaryKey):
    UniqueList = set()
    for i in ListToDisplay:
        UniqueList.add (i[PrimaryKey])
    size = len (UniqueList)
    print ("size of unique list: ", size)

ListToDisplay = FileToList (FileNameNPath)
Display (ListToDisplay)
DisplayUnique (ListToDisplay, PrimaryKey)
