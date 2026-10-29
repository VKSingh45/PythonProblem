# Program that reads a line and prints its statistics like:
#     Number of Uppercase letters :
#     Number of Lowercase letters:
#     Number of alphabets:
#     Number of digits:

line = str(input("Enter a line :"))
lowercount = uppercount = 0
digitcount = alphacount = 0
for a in line:
    if a.islower():
        lowercount += 1
    elif a.isupper():
        uppercount += 1
    elif a.isdigit():
        digitcount += 1
    if a.isalpha():
        alphacount += 1

print ("Number of Uppercase letters : ", uppercount)
print ("Number of Lowercase letters : ", lowercount)
print ("Number of alphabets : ", alphacount)
print ("Number of digits : ", digitcount)