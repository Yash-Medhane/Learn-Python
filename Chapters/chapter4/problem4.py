marks = int(input("enter the marks : "))

if(marks < 35 and marks >=0):
    print("student failed !!!")
elif(marks <=60 and marks >=36):
    print("student grade is C")
elif(marks <=90 and marks >=61):
    print("student grade is B")
elif(marks <=100 and marks >=71):
    print("student grade is A")
else:
    print("invalid marks !!!")
