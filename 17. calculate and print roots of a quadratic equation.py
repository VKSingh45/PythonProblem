import math
print("For quadratic equation ax*2+bx+c=0, enter coffient below .")
a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))
if a==0:
    print("value of", a , 'should not be zero')
    print("\n abortion !!!!!")
else:
    delta = b*b-4*a*c
    if delta>0:
        root1=(-b+math.sqrt(delta))/(2*a)
        root2=(-b-math.sqrt(delta))/(2*a)
        print("Roots are Real and unequal")
        peint("Root1=",root1,"Root2=",root2)
    elif delta==0:
        root1=-b/(2*a);
        print("Root are Real and Equal")
        print("Root1=",root1)
    else:
        print("Roots are complex and Imaginary.")