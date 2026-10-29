ch=input("Enter a single character :")
if ch>='A' and ch<='z':
    print("You entered an uppercase character.")
elif ch>='a' and ch<='z':
    print("You entered a lower case character.")
elif ch>='0' and ch<='9':
    print("You entered a digit character.")
else:
    print("You entered a special character.")
