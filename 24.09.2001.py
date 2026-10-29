def add(a,b,c):
    return a+b+c
def mulit(a,b,c):
    return a*b*c
def sub(a,b,c):
    return a+b-c
#main part
x=int(input("1.   enter first number    "))
y=int(input("2.   enter second number   "))
z=int(input("3.   enter third number    "))
choice=input("enter 1,2 or 3")
if choice == "1":
    s=add(x,y,z)
    print(s)
elif choice=="2":
    n=sub(x,y,z)
    print(n)
elif choice== "3":
    m=mulit(x,y,z)
    print(m)
else:
    print("wrong selecting")




