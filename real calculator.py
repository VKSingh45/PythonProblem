#a=(input("Enter first number:  "))
#b=(input("Enter second number: "))
choice=0
ch="Y"
while (ch== "Y"):
    print("Menu")
    print("1. AREA OF A CIRCLE")
    print("2. CIRCUMFERENCE OF A CIRCLE")
    print("3. AREA OF A RECTANGLE")
    print("4. PERIMETER OF A RECTANGLE")
    print("5. AREA OF A SQUARE")
    print("6.PERIMETER OF A SQUARE")
    
    print("7. QUIT")
    choice = int(input("enter your choice"))
    if (choice == 1):
        radius = int(input("enetr the circle's radius"))
        print("Area is",3.14*radius**radius)
    elif (choice == 2):
        radius = int(input("enetr the circle's radius"))
        print("Circumference is",2*3.14*radius)
    elif (choice==3):
        l=int(input("enter length of rectangle: "))
        b=int(input("enter breath of rectangle: "))
        r=l*b
        print("Area is",r)
    elif (choice==4):
        l=int(input("enter length of rectangle: "))
        b=int(input("enter breath of rectangle: "))
        print("Perimeter is",2*l+b)
    elif (choice==5):
        side=int(input("enter side of the square"))
        print("Area is",side*side)
    elif (choice==6):
       side=int(input("enter side of the square"))
       print("perimeter is",4*side)
    elif (choice ==7):
        print('Exiting the program ...')
    else:
        print('Error: invalid selection.')
