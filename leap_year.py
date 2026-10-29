year=int(input("Enter any Year :"))
if(year%100==0):
    if(year%400==0):
        print("Leap")
    else:
        print("Not leap")
else:
    if(year%4==0):
        print("Leap")
    else:
        print("Not leap")