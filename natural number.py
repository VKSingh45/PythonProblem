#Natural number
def calc(x):
   if (x==1):
      return 1
   else:
      return (x+calc(x-1))
n=int(input("Enter the number"))
tot=calc(n)
print("total=",tot)
