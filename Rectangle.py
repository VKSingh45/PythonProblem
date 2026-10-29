# Program to obtain length and breadth of a rectangle and calculate its area. 

def AreaRec (l,b):
    return l*b
l = float(input("Enter the Length of rectangle : "))
b = float(input("Enter the breadth of rectangle : "))
print("Rectangle Specification : ","\nLength = ",l,"\nBreadth = ",b,"\nArea of Rectangle = ",AreaRec(l,b))

