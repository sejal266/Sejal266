def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiple (a,b):
    return a*b
def divide (a,b):
    if b==0:
        return ("cannot divide by zero")
    return a/b

def calculator():
    print("select operation :+,-,*,/")
    op = input ("enter operator:")
    a=float (input('enter first number:'))
    b=float (input("enter second number:"))
    if op =="+":
        print("result:",add(a,b))
    elif op =="-"
        print("result:",subtract(a,b))
    elif op =="*"
        print("result:",multiply(a,b))
    elif op =="/"
        print("result:",divide(a,b))
    else:
        print("invalid operator")
        calculator()
               