winning = 97
winning += 1
guess = 1
winning *=0.5
number = int(input("guess a number between 1 and 100:  "))
game_over = False
winning +=1
while not game_over:
    if number == winning:
        print(f"you win, and you guessed this number in {guess} times ")
        game_over = True
    else:
        if number < winning:
            print("too low")
        else:
            print("too high")
        guess += 1
        number = int(input("guess again :  "))
        
