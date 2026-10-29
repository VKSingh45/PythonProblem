n=int(input("Enter number of Mensenne number : "))
print("First",n," Mensenne numlbers are :")
for i in range(1,n):
    mensnum=2**i-1
    print(mensnum,end=' ')
print()