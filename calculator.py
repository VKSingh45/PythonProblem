# how to make calculator .
import circle
import rectangle
choice=0
ch= "Y"
while (ch == "y"):
    print("MENU")
    print("1. AREA OF A CIRCLE")
    print("2. CIRCUMFERENCE OF A CIRCLE")
    print("3. AREA OF A RECTANGLE")
    print("4. PERIMETER OF A RECTANGLE")
    print("5. QUIT")
    choice = int(input("enter your choice"))
    if (choice == 1):
        radius = int(input("enetr the circle's radius"))
        print("The area is ",circle.area(radius))
    elif (choice == 2):
        radius = int(input("enetr the circle's radius"))
        print("circumference is",circle.circumference(radius))
    elif (choice == 3):
        l=int(input("enter the length of rectangle"))
        b=int(input("enter the breath of rectangle"))
        print("the area is",rectangle.area(l,b))
    elif (choice == 4):
        l=int(input("enter the length of rectangle"))
        b=int(input("enter the breath of rectangle"))
        print("perimeter is",rectangle.perimetr(l,b))
    elif (choice ==5):
        print('Exiting the program ...')
    else:
        print('Error: invalid selection.')
