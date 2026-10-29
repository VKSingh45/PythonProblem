num1=float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
num3=float(input("Enter third number : "))
num4=float(input("Enter fourth number : "))
num5=float(input("Enter fifth number : "))
divisor=float(input("Ente divisor number : "))
count=0
print("multiples of",divisor,"are:")
remainder=num1%divisor
if remainder==0:
    print(num1,sep=" ")
    count +=1
remainder=num2%divisor
if remainder==0:
    print(num2,sep=" ")
    count +=1
remainder=num3%divisor
if remainder==0:
    print(num3,sep=" ")
    count +=1
remainder=num4%divisor
if remainder==0:
    print(num4,sep=" ")
    count +=1
remainder=num5%divisor
if remainder==0:
    print(num5,sep=" ")
    count +=1
print()
print(count,"multiples of",divisor,"found")