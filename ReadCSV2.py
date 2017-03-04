import unicodecsv
#saves all the data as a list of dictionaries

FileNameNPath = 'C:/Users/AB/Downloads/IntroToDataAnalysis/JupyterNotebookMaterial/enrollments.csv'
#convert the backward slashes to forward ones.

def ReadFile (FileNameNPath):
    with open (FileNameNPath, 'rb') as FileObject:
        ReaderCsv = unicodecsv.DictReader (FileObject)
        #Each line is read as dictionary
        enrollments = list (ReaderCsv)
        # we create a list of the dictionaries.
        PrintByLine (enrollments)

def PrintByLine (ListOfDict):
    rows = len (ListOfDict)
    for i in range(rows):
        print (i, "->", ListOfDict[i])

ReadFile(FileNameNPath)
