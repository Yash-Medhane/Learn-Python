with open("./temp.txt",'r') as f:
    content = f.read()


if('python' in content):
    print("yes it is present")
else:
    print('not present')
