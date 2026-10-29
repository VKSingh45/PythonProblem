def Bsearch(item,key):
    low=0
    high=len(item)-1
    while low<=high:
        mid=int((low+high)/2)
        if key==item[mid]:
            return mid
        elif key < item[mid]:
            high=mid-1
        else:
           low=mid+1
    else:
        return -999
s=[54,24]
k=input("Enter Any Items :")
d=Bsearch(s,k)
if d>=0:
    print("Item Is Found : ",d)
else:
    print("Item IS Not Found : ","OOOOOOOOOOO Item Is Not Found")
        
        
