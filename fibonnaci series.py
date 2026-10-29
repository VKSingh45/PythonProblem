import platform
import os

def fib(n):
    a,b=0,1
    while a<n:
        print(a, end="")
        a,b=b,a+b
        print()
x=int(input("enter any number : "))
fib(x)

def runAgain():
    run=input("\n Want To Run Again Y/N : ")
    
    while(run.lower()=='y'):
        if(platform.system()=="Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        fib(x)
        run=input("\n Want To Run Again Y/N : ")

runAgain()
