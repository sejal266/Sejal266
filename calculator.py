a=float(input("enter a number:"))
b=float(input("enter a number:"))
operator=input("enter operator(+,-,*):")
if operator =='+':
    result=a+b
    print("Result:",result)
 elif operator == '-':
    result=a-b
    print("Result:",result)
 elif operator =='*':
    result=a*b
    print("Result:",result)
 else:
    print("invalid operator")      