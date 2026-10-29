x=float(input("Enter value of x :"))
n=int(input("Enter value of n (for x**n) :"))
s=0
for a in range(n+1):
    s+=x**a
print("Sum of first",n,"terms :",s)