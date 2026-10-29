n=int(input("Enter an integer :"))
mid=int(n/2)
print("The divisors of",n,"are :")
for i in range(2,mid+1):
    if n%i==0:
        print(i,end=' ')
else:
    print("-End-")