a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))
min=mid=max=None
if a>b and a>c:
    if b>c:
        min,mid,max=c,b,a
    else:
        min,mid,max=b,c,a
elif b>a and b>c:
    if a>c:
        min,mid,max=c,a,b
    else:
        min,mid,max=a,c,b
else:
    if a>b:
        min,mid,max=b,a,c
    else:
        min,mid,max=a,b,c
print("Ascending order numbers is :",min,mid,max)