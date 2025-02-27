a=int(input("Enter the number1: "))
b=int(input("Enter the number2: "))
s=lambda a,b:a if a>b else b
r=s(a,b)
print("Greater number is",r)