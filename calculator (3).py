def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

num1=int(input("Enter the First Number : "))
num2=int(input("Enter the Second Number : "))
ch=int(input("1. Sum of Two Numbers \n2. Subtract of Two Numbers \n3. Multiply of Two Numbers \n4. Divide of Two Numbers \nChoice The Above option : "))
if(ch==1):
    add(num1,num2)
elif(ch==2):
    sub(num1,num2)
elif(ch==3):
    mult(num1,num2)
elif(ch==4):
    div(num1,num2)
