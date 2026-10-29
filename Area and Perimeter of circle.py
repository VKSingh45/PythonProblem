# Program to display a menu for calculating area or perimeter of the circle. 

def Area(r):
    return (22/7)*r*r

def Perimeter(r):
    return (22/7)*2*r

ch = int(input("Choice Area (1) or Perimeter (2) of Circle :"))
r = float(input("Enter Radius of the Circle : "))
if (ch == 1):
    print("Area of the Circle : ", Area(r))
elif (ch == 2):
    print("Perimeter of the Circle : ", Perimeter(r))
else:
    print("Please Choice (1 or 2) not choice any other Number : ")