#Simple Interest
def inter(principal,time=2,rate=0.10):
   return principal*rate*time
n=float(input("Enter principal amount:  "))
#print("Simple Interest with default ROI and time values is:   ")
#s1=inter(n)
#print("Rs.",s1)


r=float(input("Enter rate of interest (ROI):  "))
t=int(input("Enter time in Years:    "))
s2=inter(n,t,r/100)
print("Rs.",s2)
