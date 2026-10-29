'''
Task-1:
WAP to take word input from user and display the input
in jumbled form eg.
Input – game
Output - agme
'''
import random
print("type a world ")
i=0
wordj=""
word=input()
word=str(word)
while i<len(word):
    wordj+=word[random.randrange(len(word))]
    i+=1
print(wordj)
