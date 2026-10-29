n=int(input("Enter number of fibonacci serie: "))
first=0
second=1
print(first)
print(second)
for n in range(1,n):
    third=first+second
    print(third)
    first,second=second,third