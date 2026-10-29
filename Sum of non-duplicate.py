# Program That input three numbers and calculates two sums as per this:
#     a) Sum1 as the sum of all input numbers.
#     b) Sum2 as the sum of non-duplicate numbers; if there are duplicate number in the input, ignores them.

def SumDuplicate(x,y,z):
    sum = 0
    if (x != y) and (x != z):
        sum += x
    elif (y != x) and (y != z):
        sum += z
    elif (z != x) and (z != y):
        sum += z
    print("Sum of Non-duplicate numbers is : ", sum)

x = float(input("Enter 1st Number : "))
y = float(input("Enter 2nd Number : "))
z = float(input("Enter 3rd Number : "))
print("Sum of three Number is : ", x+y+z)
SumDuplicate(x,y,z)

