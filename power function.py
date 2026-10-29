# Program to calculate a**b using iterative code.

def power(a,b):
    res = 1
    if (b==0):
        return 1
    else:
        # return a * power(a, b-1)
        for i in range(b):
            res *= a
    return res

a = int(input("Enter Number : "))
b = int(input("Enter base number : "))
print(power(a,b))