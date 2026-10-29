#program to find loop value
i=1
a=int(input("Enter any numbers(1to1000)"))
for a in range(1,a):
    i=i+a
    if a==0:
        print("you should not enter zero ")
        continue
    print(i)
