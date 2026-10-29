n=int(input("Enter number of mersenne numbers :"))
for i in range(1,n+1):
    mersnum=2**i-1
    mid=int(mersnum/2)+1
    for a in range(2,mid):
        if mersnum%a==0:
            print(mersnum)
            break
    else:
        print(mersnum, "\tPrime")