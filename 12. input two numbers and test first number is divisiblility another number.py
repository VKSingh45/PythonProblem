n=int(input("Enter first number :"))
m=int(input("Enter second number :"))
r=n%m
if r==0:
    print(n,"is divisible to",m)
else:
    print(n,"is not divisible to",m)
