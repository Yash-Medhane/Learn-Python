def natural(i,n):
    if(i > n):
        return
    print(i)
    return natural(i+1,n)

natural(1,int(input("Enter the number : ")))