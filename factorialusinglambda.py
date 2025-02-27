a=int(input("Enter the number: "))
s=lambda n:n*s(n-1)if n>1 else 1
result=s(a)
print(print("factorial of ",a,"=",result))