print("Calculator:")
a= input("Enter first element:")
c =input("Select the operator{*,/,+,-,%}:")
b=input("Enter the second element:")
a = int(a)
b = int(b)
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="%":
    print(a%b)
else:
    print("Error:")


