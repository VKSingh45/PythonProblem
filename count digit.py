#write a funstion
def f(n):
   count=0
   while (n>0):
      n=n//10
      count += 1
   return count
a=int(input("Enter a number"))
total=f(a)
print("total number of digit ",total)
