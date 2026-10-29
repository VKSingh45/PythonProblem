sum=0
n=int(input("How many terms ?"))
for a in range(2,n+2):
    term=0
    for b in range(1,a):
        term+=b
    print("Term",(a-1),":",term)
    sum+=term
print("Sum of",n,"terms is",sum)