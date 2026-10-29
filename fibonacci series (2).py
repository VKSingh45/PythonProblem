# How to make fibonacci series.
def fibo(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        return (fibo(x-1)+fibo(x-2))
n=int(input("enter any natural number:  "))
for i in range(1,n+1):
    print(fibo(i))
