string=input("Enter a string :")
length=len(string)
maxlength = 0
maxsub =''
sub=''
lensub = 0
for a in range(length):
    if string[a] in 'aeiou' or string[a] in 'AEIOU':
        if lensub > maxlength:
            maxsub = sub
            maxlength = lensub
            sub=''
            lensub =0
    else:
        sub += string[a]
        lensub = len(sub)
    a +=1
print("Maximum length consonant substring is :",maxsub,end=' ')
print("with",maxlength,"characters")