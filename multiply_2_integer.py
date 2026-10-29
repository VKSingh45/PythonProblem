n=int(input("Enter 1st number: "))
m=int(input("Enter 2nd number: "))
cnt=n
prd=0
while cnt>0:
    cnt=cnt-1
    prd += m
print("{} X {} = {}".format(n,m,prd))