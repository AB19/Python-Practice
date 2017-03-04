FileObject = open ("SampleStuff.txt", 'a')
FileObject.write ("jaffa")
FileObject.write ("\n\tdaffa")
FileObject.write ("\nkulfi")
FileObject.close()


fr = open ("SampleStuff.txt", 'r')
text = fr.read()
print (text)
fr.close()
