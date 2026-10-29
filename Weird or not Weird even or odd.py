n=int(input())
for i in range(1,n+1):
    if((n>=2)&(n<=5)):
        if(n%2!=0):
            print("Weird")
            break
        else:
            print("Not Weird")
            break
    else:
        if((n>=6)&(n<=20)):
            if(n%2==0):
                print("Weird")
                break
            elif(n%2!=0):
                print("Weird")
                break
        elif(n>=20):
            if(n%2==0):
                print("Not Weird")
                break
            elif(n%2!=0):
                print("Weird")
                break
            
