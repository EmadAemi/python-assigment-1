from cmath import sqrt
import math
a = int(input("First Number: "))
operation = input("Operation (+, -, *, /, radical, sin, cos, tan, cot, factoriel): ")
if operation=='radical' or operation=='sin' or operation=='cos' or operation=='tan' or operation=='cot' or operation=='factoriel':
    if operation=='radical':
        print(math.sqrt(a))
    elif operation=='sin':
        print(math.sin(a/(180/math.pi)))
    elif operation=='cos':
        print(math.cos(a/(180/math.pi)))
    elif operation=='tan':
        print(math.tan(a/(180/math.pi)))
    elif operation=='cot':
        print(math.cot(a/(180/math.pi)))
    elif operation=='factoriel':
        print(math.factorial(a))
elif operation=='+' or operation=='-' or operation=='*' or operation=='/':
    b = int(input("Second Number: "))
    if operation=='+':
        print(a+b)
    elif operation=='-':
        print(a-b)
    elif operation=='*':
        print(a*b)
    elif operation=='/':
        if b==0:
            print("Divison by zero")
        else:
            print(a/b)
else:
    print("Non-defiuned operator")