#defining Variables

from audioop import avg


day = 0
squats = 0
total = 0
print("Enter the number of squats you did on each day for the last one week...and don't lie! \n")

#while loop and the loop body.

while (day<=6):
    day =day+1
    squats = int(input("Squats on day {} :".format(day)))
    total=total+squats

#statements outside of the while loop

avg = total/day
print("In the last {} days, you did an average of {} squats ".format(day,avg))