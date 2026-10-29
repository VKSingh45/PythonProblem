"""Task-1:
	Create a program wages.py that assumes people are paid double time for hours over 60. They get paid for at most 20 hours overtime at 1.5 times the normal rate. 
	For example, a person working 65 hours with a regular wage of $10 per hour would work at $10 per hour for 40 hours, at 1.5 * $10 for 20 hours of overtime, and 2 * $10 for 5 hours of double time, for a total of
	10*40 + 1.5*10*20 + 2*10*5 = $800.
	The number of hours should be generated randomly between 35 and 75.
	If the number of working hours is less than 40, display message “The salary cannot be generated” with sound of system bell as a warning.
"""

workhour=int(input("Enter the total hour of work : "))
if (workhour <= 0) :
    print("\nPlease enter a value greater than 0")

print("Total work hour is :",workhour,"hours")    
if (workhour <=40):
    income1=int(workhour)*10
    print("Total income generated is :",mlp,"$")

elif (workhour>40):
      remaining=int(workhour)-40
      if remaining<=20:
          income2=40*10+ int(remaining)*1.5*10
          print("The total income generated is ",income2,"$")

elif (remaining>20):
            extra=int(workhour)-40-20
            income3=40*10+20*10*1.5+int(extra)*10*2
            print("The total income genarated is",income3,"$")
