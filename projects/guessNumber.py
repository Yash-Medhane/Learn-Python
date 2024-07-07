from random import randint


def randomNumber():
    return randint(1,100)

def check(userNumb,compNumb):
    if(userNumb == compNumb):
        return "You Win"
    elif(userNumb < compNumb):
        return "Try again Hint: Number is greater"
    elif(userNumb > compNumb):
        return "Try again Hint: Number is smaller"
    else:
        return "something went wrong !!!"

def takeNumb():
    return int(input("Guess the number : "))

number = randomNumber()

while(True):
    n= int(input("Guess the number : "))
    check(n,number)
    print(check(n,number))
    if(check(n,number) == "You Win"):
        break