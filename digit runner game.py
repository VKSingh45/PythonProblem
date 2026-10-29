def game():
    print("Welcome to -:) DIGIT  RUNNER (:- game.\n")
    print("\n1.Enter any digit to make the sign move.\n2.Number should not than be than 10.\n3.Enter EXIT to quit game\n")
    sign:str=">"
    num=int(input("Enter the number :\n"))
    print(">")
    if num>10:
        print("choose within the range:\n")
    else:
        for i in range(num+1):
            print(num*""+sign)
            num=int(input())
            if num>10:
                print("Choose within the range \n")
            else:
                print(num*""+sign)
                continue


game()
