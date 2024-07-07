def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y!=0:
        return x/y
    else:
        print('infinte')

is_loop = True

while is_loop:
    a=float(input("first value : "))
    b=float(input("second value : "))
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter choice (1/2/3/4): "))
    if choice == 1:
        print(f"Ans: {add(a,b)}")
    elif choice == 2:
        print(f"Ans: {sub(a,b)}")
    elif choice == 3:
        print(f"Ans: {mul(a,b)}")
    elif choice == 4:
        print(f"Ans: {div(a,b)}")
    else:
        print("invalid input")
    
    if '1'==input("enter 1 to continue : "):
        is_loop=True
    else:
        is_loop=False