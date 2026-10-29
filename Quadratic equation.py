# Program to calculate and print roots of a quadratic equation ax^2 + bx + c = 0 (a != 0).

import math

def Quad(a,b,c):
    if (a==0):
        print("Value of ", a , " Should not be zero. \n\nAborting !!!!!")
    else:
        d = b*b - 4*a*c
        if (d > 0):
            r1 = (-b + math.sqrt(d))/(2*a)
            r2 = (-b - math.sqrt(d))/(2*a)
            print("Roots are Real and Unreal \n Root1 = ",r1 , "Root2 = ",r2)
        elif (d == 0):
            r1 = -b/(2*a)
            print("Roots are Real and Unreal \n Root1 = ", r1 , "Root2 = ",r2)
        else:
            print("Roots are complex and Imaginary. ")

print("For Quadratic equation ax^2 + bx + c = 0, Coffieient below!")
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
Quad(a,b,c)
