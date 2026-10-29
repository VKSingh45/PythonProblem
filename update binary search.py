#binary search
def bsearch(arr,key):
   low=0
   high=len(arr)-1
   while low<=high:
      mid =int((low+high)/2)
      if key==arr[mid]:
         return mid
      elif key<arr[mid]:
         high=mid-1
      else:
         low =mid+1
   else:
      return -999

arr=[2,3,4,10,40,45]
item=int(input("enter the item will search:  "))
r=bsearch(arr,item)
if r >=0:
   print("Element is present at index ",r)
else:
   print("Element is not present in array")
