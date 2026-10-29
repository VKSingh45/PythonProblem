
x=int(input("Enter first number :"))
y=int(input("Enter second number :"))
z=int(input("Enter third number :"))
while x==y==z:
    print(" All numbers are Same",x,y,z)
    break
else:
    if x==y!=z or x!=y==z:
        sum=x+z
    elif x!=y!=z and x!=z!=y:
        sum = x+y+z
    else:
        sum = x+y
    print("sum of numbers is",sum)
