# Write a program to obtain a days, hours, minutes & seconds and Calculate time. The amount of seconds.

def AmountSec():
    return d + h + m + s 

d = int(input("Enter Days : ")) * 3600 * 24
h = int(input("Enter Hours : ")) * 3600
m = int(input("Enter Minutes : ")) * 60
s = int(input("Enter Seconds : "))
print("The Amount of Seconds : ", AmountSec())