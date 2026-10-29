def bsearch(arr,key):
   low=0
   high=len(arr)-1
   while low<=high:
      mid =int((low+high)/2)
      if key == arr[mid]:
         return mid
      elif key<arr[mid]:
         high=mid-1
      else:
         low=mid+1
   else:
      return -999

arr =[4,10,15,27,34,48,50]
item=int(input("Enter item search:  "))
r=bsearch(arr,item)
if r>=0:
   print("item is found",r)
else:
   print("item is not found")
      
