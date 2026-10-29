sum=sum1=0
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=int(input("Enter third number: "))
sum1 = x+y+z
if x!=y and x!=z:
    sum += x
if y!=x and y!=z:
    sum += y
if z!=x and z!=y:
    sum += z
print("Numbers are",x,y,z)
print("Sum of three numbers is",sum1)
print("sum of non-duplicate numbers is",sum)