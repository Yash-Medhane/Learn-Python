class emp:
    name=''
    percentage=0

    def __init__(self):
        print("object is created")
        
    def getdata(self,name,percentage):
        print(f"{name} : {percentage} %")

yash = emp()
yash.getdata('yash',85)