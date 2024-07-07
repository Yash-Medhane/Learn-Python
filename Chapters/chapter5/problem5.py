n=50

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" " ,end="")
#     for j in range(i):
#         print("*" ,end="")
#     for j in range(n-i):
#         print(" " ,end="")
#     print('\n')

for i in range (1,n+1):
    print(" "*(n-i),end="")
    print("Yash"*(2*i-1),end="")
    print("")