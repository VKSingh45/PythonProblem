lst=[]
r=int(input("Enter Any Number : ")
      )
c=int(input("Enter Any Number :"))
for k in range(r):
    row=[]
    for l in range(c):
        elem=int(input("Element"+str(k)+str(l)+" : "))
        row.append(elem)
    lst.append(row)
print('\t',"list Created is : " , lst)
"""for i in range(r):
    print("\t[",end="")
    for j in range(c):
        print(lst[i][j],end="")
        print("]")"""
