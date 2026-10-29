count=sum=0
ans='y'
while ans=='y':
    num=int(input("Enter number: "))
    if num<0:
        print("Number entered is below Zero. Aborting!")
        break
    sum=sum+num
    count=count+1
    ans=input("Want to enter more numbers? (y/n)..")
else:
    print("You entered",count,"numbers so far.")
print("Sum of numbers entered is",sum)