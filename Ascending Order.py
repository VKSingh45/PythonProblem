# Program that reads three numbers and print them in ascending order.

a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
c = int(input("Enter 3rd Number : "))
min,mid,max = None
if (a>b) and (a>c):
    if (b>c):
        min,mid,max = c,b,a
    else:
        min,mid,max = b,c,a
elif (b>a) and (b>c):
    if (a<c):
        min,mid,max = c,a,b
    else:
        min,mid,max = a,c,b
else:
    if (a>b):
        min,mid,max = b,a,c
    else:
        min,mid,max = a,b,c

print("Ascending order Number is : ", min,mid,max)