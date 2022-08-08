import math
class perimeter:

    def rect(self,a,b):
        print("Area of rectangle "+str(a*b))
        print("Perimeter of Rectangle "+str(2*(a+b)))
    def circle(self,r):
        print("Area of circle "+str(math.pi*math.pow(r,2)))
        print("perimeter of circle "+str(2*math.pi*r))
    def triangle(self,a,b,c):
        h=math.sqrt((a*a)+(b*b))
        print("Area of Triangle "+str((1/2)*b*h))
        print("Perimeter of Triangle "+str(a+b+c))
obj=perimeter()
print("Enter Number of inputs:")
ch=int(input())
if(ch==1):
    obj.rect(int(input("Enter 1st Side:")), int(input("Enter 2nd Side:")))
elif(ch==2):
    obj.circle(int(input("Enter Radius:")))
elif(ch==3):
    obj.triangle(int(input("Enter 1st Side:")), int(input("Enter 2nd Side:")),int(input("Enter 3rd Side:")))
elif(ch==4):
    obj.triangle(int(input("Enter 1st side:")), int(input("Enter 2nd side:")), int(input("ENter 3rd side:")))
elif(ch==5):
    obj.triangle(int(input("Enter 1st side:")), int(input("enter 2nd side:")),int(input("Enter 3rd side:")))
elif(ch==6):
    obj.triangle(int(input("Enter 1st side:")), int(input("ENter 2nd side:")), int(input("Enter 3rd side")))
elif(ch==7):
    obj.triangle(int(input("Enter 1st side:")), int(input("Enter 2nd side")), int(input("Enter 3rd side:")))

