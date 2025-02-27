def mul(n):
    if(n==1):
       return 1
    else:
        return n*mul(n-1)
a=int(input("Enter the Number: "))
result=mul(a)
print("Multiplication of ",a,"=",result)