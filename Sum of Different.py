# Program that input three numbers and print sum of different numbers, Same numbers will show message all the numbers 
# and same and break the program.

def SumNum (x,y,z):
    if (x==y==z):
        return ("All Numbers are Same.")
    else: 
        if (x==y!=z) or (x!=y==z):
            return x+z
        elif (x!=y!=z) and (x!=z!=y):
            return x+y+z
        else:
            return x+y

x = int(input("Enter 1st Number : "))
y = int(input("Enter 2nd Number : "))
z = int(input("Enter 3rd Number : "))

print(SumNum(x,y,z))