num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))
op=input("Enter operator [ + - * / % ]:")

if op=='+':
    result=num1+num2
elif op=='-':
    result=num1-num2
elif op=='*':
    result=num1*num2
elif op=='/':
    result=num1/num2
elif op=='%':
    result=num1%num2
else:
    print("Invalid operator!!")
print(num1,op,num2,'=',result)
