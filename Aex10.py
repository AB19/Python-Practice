#Calculator that performs + - * /

def Addition (x,y):
    Value = x + y
    print (Value)

def Subtraction (x,y):
    Value = x - y
    print (Value)

def Multiplication (x,y):
    Value = x * y
    print (Value)

def Division (x,y):
    Value = x / y
    print (Value)

print ("Enter the operand")
FirstOp = int(input())
print ("Enter another")
SecondOp = int(input())
print ("Enter the Operation + for addition .......")
Operation = input()

if (Operation == '+'):
    Addition(FirstOp,SecondOp)
elif (Operation == '-'):
    Subtraction(FirstOp,SecondOp)
elif (Operation == '*'):
    Multiplication(FirstOp,SecondOp)
elif (Operation == '/'):
    Division(FirstOp,SecondOp)
