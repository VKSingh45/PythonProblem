#write a program to add two more students details to the file created . in pg-186
fileout=open("marks.det","a")
for i in range(2):
   print("Enter details for student",(i+1),"below:")
   rollno=int(input("Rollno:  "))
   name=input("Name:  ")
   marks=float(input("Marks:  "))
   rec = str(rollno)+","+name+","+str(marks)+'\n'
   fileout.write(rec)
fileout.close()
