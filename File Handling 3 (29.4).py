f=open("Student_INFO.txt",'w')
i=int(input("Enter number of students in the class."))
for a in range(i):
    nm=str(input("Enter name of student."))
    f.write(nm)
f.close()
