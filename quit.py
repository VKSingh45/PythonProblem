def user_quit():
    a=input("Enter 'q' to exit the program :")
    b=a.lower()
    if (a=='q'):
        print()
    else:
        game()
    return 0





import random
def user_num():
    a=int(random.randrange(1,15))
    
    return 0


def game():
    sign:str=">"
    print(">")
    a=user_num()
    if (a>10):
        print("Choice within range \n")
    else:
        
       
        for i in range(a):
            print(a*" "+sign)
            a=user_num()
            if (a>10):
                print("Choice within range \n")
            else:
                print(a*" "+sign)
                c= user_quit()


game()
