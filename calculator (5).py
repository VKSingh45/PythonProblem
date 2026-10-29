n=eval(input("Enter the first number : "))
m=eval(input("Enter the Second number : "))
ch=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\nEnter any option :"))
if(ch==1):
    print("{} + {} = {}".format(n,m,n+m))
elif(ch==2):
    print("{} - {} = {}".format(n,m,n-m))
elif(ch==3):
    print("{} X {} = {}".format(n,m,n*m))
elif(ch==4):
    print("{} / {} = {}".format(n,m,n/m))
else:
    print("Please select correct option")