class complexx:

    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c2):
        return complexx(self.r+c2.r , self.i+c2.i)
    def __str__(self):
        return f"{self.r} + {self.i}i"
    @staticmethod
    def add():
        print("this is the complex number :")
    
c1 = complexx(1,2)
c2 = complexx(3,4)
c1.add()
print(c1+c2)
