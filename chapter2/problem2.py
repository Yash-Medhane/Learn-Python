markes = []

for i in range(1,6):
    m=int(input("enter the marks : "))
    markes.append(m+i)

markes.sort()
print(markes)
print("sum : ",sum(markes))