email=input("Enter your email id :")
domain='@edupillar.com'
ledo=len(domain)
lema=len(email)
sub=email[lema-ledo :]
print(sub)
print(lema,ledo,lema-ledo,email)
if sub==domain:
    if ledo !=lema:
        print("It is valid email id")
    else:
        print("It is Invalid email id")
else:
    print("this email-id is either not Valid or belong to some other domain")