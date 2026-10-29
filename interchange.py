"""
Two Number are input through the Keyboard into
two location c and d. Write a program to interchange
the contents of c and d.
"""
c=int(input("Enter the First number : "))
d=int(input("Enter the Second number : "))
c=c+d

d=c-d

c=c-d

print("First Number after interchange is : ",c)
print("Second Number after interchange is : ",d)
