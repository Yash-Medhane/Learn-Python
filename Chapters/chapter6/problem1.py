
def fac(n):
    if(n < 2):
        return n
    return fac(n-1)+fac(n-2)

n= int(input("enter the number : "))

for i in range(n+1):
    print(fac(i))