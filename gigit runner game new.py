'''def game():
    print("Welcome to -:) DIGIT  RUNNER (:- game.\n")
    print("1.Enter any digit to make the sign move.\n2.Number should not than be than 10.\n3.Enter EXIT to quit game\n")
    num=int(input("Enter the Number less than 10 :"))
    sign:str=">"
    if ((num>10)&(num<0)) :
        print("chooce within the range :\n")
    else:
        for i in range(1,num+1):
            
            print(sign)

            num=input()
            if (num=='q'):
                print("Good Bye @@@@@")
            else:
                if ((num>10)&(num<0)):
                    print("chooce within the range :\n")
                elif ((num>=0)&(num<=10)):'''
                      

def user_digit():
    num=int(input("Enter The Number :"))
def user_exit():
    num=input("run the program (Yes \t No) press :- \n\t y or n")
    a=num.lower()
    if a=='n':
        print()
    elif a=='y':
        user_digit()
    else:
        print("choose correct option")


user_exit()
