def max_num(x,y,z):
    if ((x>y)&(x>z)):
        print(x,"is Greatest number")
    elif ((y>x)&(y>z)):
        print(y,"is Greatest number ")
    elif ((z>y)&(z>x)):
        print(z,"is Greatest number ")
    else:
        if ((x==y)&(y==z)):
            print("All Number are Same ")
        else:
            print("Two number is same")
    print("\n",x,y,z)
a=int(input("Enter The First Number : "))
b=int(input("Enter The Second Number : "))
c=int(input("Enter The Third Number : "))
print(max_num(a,b,c))























'''
Write a menu driven program that allow the user to perform any one of the following operations based on the input given by user

i       Check number is even or odd

ii      Check number is positive or negative

iii     Printing square of the number

iv     Printing square root of the number (use math.h)

Use switch statement for a menu driven program. Also, use validation checks wherever necessary.

10:04 AM
practical 3.2

'''
