# global and local variables

print ("Enter a value")
x = int(input())
print ("Enter another")
y = int(input())


def change(m,n):

    global x, y
    x = x + y
    n = m + 1
    print (x,n)

change(x,y)


print (x,y)
