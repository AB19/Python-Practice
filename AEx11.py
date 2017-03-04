#lists take in values an print

StudentNames = []
print ("How many students?")
Num = int(input())
i = 0
while (i < Num):
    StudentNames = StudentNames + [input()]
    print(StudentNames[i])
    print(i)
    i = i+1

print (StudentNames)


spam = []

spam[0] = 22
# wont work. until there is a value there, you can replace it :P hence will throw index out
#of range error
print (spam)
