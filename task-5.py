def wages():
    try:
        val = int(input("Enter the Time of work :\n"))
        if val<=40:
            salary=int(val)*10
            print("your Salary is", salary)
        elif val>40:
            time=int(val)-40
            salary=40*10+int(time)*1.5*10
            print("Your Salary is ",salary)
    except valueError:
        print("Please enter valid operation ")

wages()
