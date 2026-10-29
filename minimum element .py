lst=eval(input("enter the value for the list"))
leng=len(lst)
min.num=lst[0]
min.index=lst[0]
for i in range(1,leng):
        if lst[i]<min.num:
                min.num=lst[i]
                min.index="i"
print("minimum is =",minimum,"presental",min.index)
