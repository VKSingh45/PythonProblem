f=open("stud.txt",'w')
for i in range (5):
    nm=str(input("Enter a name."))
    f.write(nm)
f.close()
