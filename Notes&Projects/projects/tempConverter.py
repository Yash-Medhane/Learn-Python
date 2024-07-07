def Fahrenheit(x):
    return ((9/5)*x)+32

def Celsius(x):
    return (5/9)*(x-32)

temp = float(input("Enter the temp : "))

print("1.celsius to farenhit")
print("2.farenhit to celcius")
print("enter any other number to exit")

choice = int(input("Enter the choice : "))

if choice==1:
    print(f"Fahrenheit : {Fahrenheit(temp)}")
elif choice==2:
    print(f"Celsius : {Celsius(temp)}")
else:
    print("your program is terminated!!!")