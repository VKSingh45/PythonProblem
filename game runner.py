
def game():
    print("Welcome to DIGIT RUNNER game\n")
    print("""
1. Enter any digit to make the sign move.
2.number should not be more than be than 10.
3.enter exit to quit game.
""")
    sign:str = ">"
    num = int(input("Enter the Number :\n"))
    print(">")
    if num > 10:
        print("Choice within the range !!!")
    else:
        for i in range(num+1):
            print(num*" "+sign)
            a=int(input())
            if a > 10:
                print("Choice within the range !!!")
            else:
                print((num*" ")+(a*" "+sign))
                continue
        
            


game()
