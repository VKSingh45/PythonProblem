r =float(input("Enter radius of the circle :"))
print("1. Calculate Area")
print("2. Calculate perimeter")
choice =int(input("Enter 1 and 2 :"))
if choice ==1:
    a = 3.14159*r*r
    print("Area of circle with radius",r ,' is ',a)
elif choice ==2:
    p = 2*3.14159*r
    print("Perimeter of circle with radius",r ,' is ', p)
else:
    print("Please Choice (1 or 2) not choice any other numbers")

    