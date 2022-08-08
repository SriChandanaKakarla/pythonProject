class calculate:
    def __init__(self,length,breadth):
        self.lengthl=length
        self.breadth=breadth
    def perimeterRect(self):
                   return(2*self.length*self.breadth)
    def areaRect(self):
         return(self.length*self.breadth)

    def __init__(self,radius):
        self.radius=radius
        def perimeterCircle(self):
            return(2*3.14*radius)
        def areaCircle(self):
            return(3.14*radius*radius)

    def __init__(self, side,breadth,heigth):
        self.side=side
        self.breadth=breadth
        self.height=height

    def perimeterTriangle(self):
            return(3*side)
        def areaTriangle(self):
         return(breadth*height)

l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
r = int(input("Enter radius of Circle: "))
obj1=calculate(l,b)
obj2=calculate(r)
print("Area of rectangle:",obj1.areaRect())
print("Perimeter of rectangle:",obj1.perimeterRect())
print("Area of Circle:",obj2.areaCircle())
print("Perimeter of Circle:",obj1.perimeterRect())