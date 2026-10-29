for i in range(15,25):
    for j in range(2,i):
        if i%j==0:
            k=i/j
            print("Found a factor (",j,") for",i)
            break
    else:
        print(i,"is a prime number")