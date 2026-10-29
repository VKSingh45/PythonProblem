# Program using two function and calculate sum and average of three numbers.

def calsum(a,b,c):
    return a+b+c
def average(a,b,c):
    return calsum(a,b,c)/3

a = float(input("Enter 1st  Number : "))
b = float(input("Enter 2nd  Number : "))
c = float(input("Enter 3rd  Number : "))
print("Average of these numbers is ", average(a,b,c))