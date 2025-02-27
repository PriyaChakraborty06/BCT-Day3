def sum(n):
    if(n==1):
       return 1
    else:
        return n+sum(n-1)
a=int(input("Enter the Number: "))
result=sum(a)
print("Sum of ",a,"=",result)