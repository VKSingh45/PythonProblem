'''
Task-4:
Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500)
against a given amount
'''
amount=int(input("Enter the amount :"))


nofhun=amount//500
amount%=500
nothun = amount//200
amount%=200
nohun=amount//100
amount%=100
nofifty =amount//50
amount%=50
notwe=amount//20
amount%=20
noten=amount//10
amount%=10
nofive=amount//5
amount%=5
notwo=amount//2
amount%=2
none=amount//1
amount%=1
totalnotes=noten+notwe+nofifty+nohun+nothun+nofhun+nofive+notwo+none
print("Total Notes = ",totalnotes)
