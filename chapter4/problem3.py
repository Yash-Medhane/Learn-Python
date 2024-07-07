l = ['yash','anjali','ansh','anshika']

name = input("enter the name : ")

if (name.lower() in l):
    print(f'hello {name}')
else:
    print("name is not present in list")