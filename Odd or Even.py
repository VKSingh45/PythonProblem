# Program that takes a numbers and check wheater the given number be odd and even.

def OddEven(n):
    if (n%2 == 0):
        print(n, " is Even Number.")
    else:
        print(n, " is Odd Number.")

n = int(input("Enter any Number : "))
OddEven(n)