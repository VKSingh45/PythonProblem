# Program to test the divisibility of a number with another number.

def Div(n,m):
    r = n % m
    if r == 0:
        print (n," is divisble by ", m)
    else:
        print (n," is not divisble by ", m)

n = int(input("Enter 1st Number : "))
m = int(input("Enter 2nd Number : "))
Div(n,m)