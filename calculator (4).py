import math
print("1.ADDITION\n2.SUBRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.SQUARE\n6.CUBE\n7.SQUARE ROOT\n8.POSITIVE or NEGATIVE\n9.EVEN or ODD\n10.EXIT\n")
choice=int(input("Enter your choice:\n"))
if ((choice >=1)&(choice<=4)):
    num1=int(input("Enter a first number :"))
    num2=int(input("Enter a second number :"))
    if (choice==1):
        print(num1,"+",num2,"=",num1+num2)
    elif (choice==2):
        print(num1,"-",num2,"=",num1-num2)
    elif (choice==3):
        print(num1,"X",num2,"=",num1*num2)
    else:
        print(num1,"/",num2,"=",num1/num2)
if ((choice>4)&(choice<=9)):
    num1=int(input("Enter Any number :"))
    if (choice==5):
        print(num1,"=",num1*num2)
    if (choice==6):
        print(num1,"=",num1*num1*num1)
    if (choice==7):
        print(num1,"=",math.sqrt(num1))
    if (choice==8):
        if (num1>0):
            print(num1,"is postive Number ")
        else:
            print(num1,"is negative Number")
    if (choice==9):
        if (num1%2==0):
            print(num1,"is Even Number")
        else:
            print(num1,"is Odd Number")
if (choice==10):
    input("Press Enter To Exit this program")
