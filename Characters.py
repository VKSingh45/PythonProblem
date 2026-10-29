# Program to print whether a given character is an uppercase or a lowercase character or a digit or any character.

c = input("Enter a Single character : ")
if (c >= 'A') and (c <= 'Z'):
    print("You entered a uppercase character. ")
elif (c >= 'a') and (c <= 'z'):
    print("You entered a lowercase character. ")
elif (c >= '0') and (c <= '9'):
    print("You entered a digit. ")
else:
    print("You entered a special character. ")