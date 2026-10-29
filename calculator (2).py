# create a four function calculator (+,-,*,/) depending upon user choice.
#there should two number as input and print accordingly.
a=int(input("enter the first number:   "))
b=int(input("enter the second number:  "))
print("1.addition ")
print("2.substraction ")
print("3.multiplication ")
print("4.Division ")
choice=int(input("Enter the value from (1,2,3,4)"))
if choice==1:
    s=a+b
    print("sum  of two value=",s)
elif choice==2:
    sub=a-b
    print("substraction  of two value=",sub)

elif choice==3:
    m=a*b
    print("multiplication of two value=",m)
elif choice==4:
    d=a/b
    print("Division of two value=",d)
else:
    print("if you want to new calculator")
