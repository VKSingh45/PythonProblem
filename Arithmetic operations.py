# Program that receives two numbers in a function and returns the results of all arithmetic operation (+,-,*,/,%) on these numbers.

def calc(x,y):
    return x+y,x-y,x*y,x/y,x%y

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
add, sub, mult, div, mod = calc(num1,num2)
print("Sum of given numbers : ", add)
print("Subtraction of given Number : ", sub)
print("Product of given numbers : ", mult)
print("Division of given Numbers : ", div)
print("Modulo of given Numbers : ", mod)