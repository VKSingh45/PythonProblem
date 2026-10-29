# Program using a recursive function to print Gcd upto pth and qth terms.

def gcd(p,q):
    if (q==0):
        return p
    return gcd(q,p%q)

p = int(input("Entre any number : "))
q = int(input("Enter any Number : "))
print(gcd(p,q))