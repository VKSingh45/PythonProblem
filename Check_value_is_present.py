#dictionary
dir1={'Riya':'csc','uttam':'mba','aman':'iit','ayansh':'junior'}
n=input("Enter value :")
if n in dir1.values():
    for a in dir1:
        if dir1[a]==n:
            print("The key of given value is {}. ".format(a))
            break
    else:
        print("{} does not exist in dictionary.".format(n))
