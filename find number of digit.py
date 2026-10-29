def f(n):
   count =0
   while n>0:
      n%10
      count = count+1
      n=n/10
      return count
a=int(input("Enter a number"))
total=f(a)
print("total number of digit in it",total)
