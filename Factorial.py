# Program using a recursive function to print factorial upto nth terms.

def fact(n):
    if(n<2):
        return 1
    return n*fact(n-1)

n = int(input("Enter any Number : "))
print(fact(n)) 