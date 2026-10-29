import os
import platform
import mysql.connector as sql
mydb=sql.connect(host="localhost",user="root",password="",database="Fee_management")
cursor=mydb.cursor()
#insert some data.
def f_insert():
    L=[]
    print("Enter The Student Information (Roll Number, Name, Age, Class, Address)")
    roll=int(input("\tEnter Roll Number : "))
    L.append(roll)
    name=input("\tEnter Name : ")
    L.append(name)
    age=int(input("\tEnter The Age : "))
    L.append(age)
    clas=input("\tEnter Class And Section : ")
    L.append(clas)
    addr=input("\tEnter The Address : ")
    L.append(addr)
    s=(L)
    sql="insert into student (Roll,Name,Age,Class,Address)values(%s,%s,%s,%s,%s)"
    cursor.execute(sql,s)
    mydb.commit()
#view data
def F_view():
    print("\nSelect The Search critertia :\t\n\t1.Roll Number\n\t2.Name\n\t3.Age\n\t4.Address\n\t5.All")
    ch=int(input("Enter The Choice the Above Option : "))
    if(ch==1):
        s=int(input("\tEnter  Roll Number : "))
        r1=(s,)
        sql="select*from student where Roll=%s;"
        cursor.execute(sql,r1)
    elif(ch==2):
        s=input("\tEnter  Name : ")
        r1=(s,)
        sql="select * from student where Name=%s;"
        cursor.execute(sql,r1)
    elif(ch==3):
        s=int(input("\tEnter  Age = "))
        r1=(s,)
        sql="select * from student where Age=%s;"
        cursor.execute(sql,r1)
    elif(ch==4):
        s=input("\tEnter Address = ")
        r1=(s,)
        sql="select * from student where Address=%s;"
        cursor.execute(sql,r1)
    elif(ch==5):
        sql="select * from student;"
        cursor.execute(sql)
    else:
        print("Please Choice Correct Option !!!!!!")
        
    res=cursor.fetchall()
    print("The Student Details are as follows : \n(Roll Name   Age  Class Address     )")
    for x in res:
        print(x)

#insert fee deposite
def infee_dep():
    L=[]
    roll=int(input("Enter Roll Number : "))
    L.append(roll)
    fee_deposite=float(input("Enter Fee to be deposite : "))
    L.append(fee_deposite)
    month=int(input("Enter Month of Fee : "))
    L.append(month)
    s=(L)
    sql="insert into fee(Roll,fee_deposite,month)values(%s,%s,%s);"
    cursor.execute(sql,s)
    mydb.commit()

#View fee Deposite
def vfee_dep():
    r=int(input("Enter Roll Number to Check the Details for student : "))
    s=(r,)
    sql="select student.Roll,student.Name,student.Class,sum(fee.fee_deposite),fee.Month from student INNER JOIN fee on student.Roll=fee.Roll;"
    cursor.execute(sql,s)
    res=cursor.fetchall()
    print("The Student Details Are As Follows : \n(Roll Name    Class   Fee Deposite  Month) ")
    for x in res:
        print(x)
#Remove Student Details
def removedata():
    roll=int(input("Enter Roll Number of the student to delete : "))
    s=(roll,)
    sql="Delete from fee where Roll=%s;"
    sq="delete from student where Roll=%s;"
    cursor.execute(sql,s)
    cursor.execute(sq,s)
    mydb.commit()

#Menu Part
def Menu():
    print("1. Insert Student Details\n2. View Student Details\n3. Insert Fee Deposite Details\n4.View Fee Deposite Details\n5.Delete Student And Fee Details")
    ch=int(input("Choice any Option : "))
    if(ch==1):
        f_insert()
    elif(ch==2):
        F_view()
    elif(ch==3):
        infee_dep()
    elif(ch==4):
        vfee_dep()
    elif(ch==5):
        removedata()
    else:
        print("Press Correct Number ")

#password
def runAgain():
    run=input("\n Want To Run Y/N : ")
    while(run.lower()=='y'):
        if(platform.system()=="Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menu()
        run=input("\n Want To Run Again Y/N : ")
runAgain()
