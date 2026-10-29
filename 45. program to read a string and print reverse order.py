string1=input("Enter a string :")
print("The ",string1,"in reverse order is :")
length=len(string1)
for a in range(-1,(-length-1),-1):
    print(string1[a])