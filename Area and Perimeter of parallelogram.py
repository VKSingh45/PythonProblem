# Write a Program to read base/ length (l), width (w), and height (h) of parallelogram and calculate its area and perimeter. 

# Area of Parallelogram
def AreaPall(l,h):
    return l*h

# Perimeter of Parallelogram
def PeriPall(l,w):
    return (2*l) + (2*w)

ch = int(input("Choice Area (1) or Perimeter (2) : "))
l = float(input("Enter Length of Parallelogram : "))
if (ch == 1):
    h = float(input("Enter Height of Parallelogram : "))
    print("Area of Parallelogram : ", AreaPall(l,h))
elif (ch == 2):
    w = float(input("Enter Width of Parallelogram : "))
    print("Perimeter of Parallelogram : ",PeriPall(l,w))
