#How to make fabonacci series program in python
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
b=int(input("Enter any number"))
for i in range(1,b+1):
    r=fib(i)
    print(r,end=',')
print("...")

