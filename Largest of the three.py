# Program to accept three integers and print the largest of the three. make use of only if statements.

def LargestNum(x=0,y=0,z=0):
    max = x
    if (y > max ):
        max = y
    elif (z > max ):
        max = z
    return max

x = float(input("Enter 1st Number : "))
y = float(input("Enter 2nd Number : "))
z = float(input("Enter 3rd Number : "))
print("Largest Number is : ",LargestNum(x,y,z))