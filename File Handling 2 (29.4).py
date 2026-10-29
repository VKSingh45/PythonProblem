f=open("employee.txt",'w')
for i in range(10):
    nm=str(input("Enter employee name."))
    f.write(nm)
f.close()
