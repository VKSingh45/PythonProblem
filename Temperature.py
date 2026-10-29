# Write a program to obtain temperature in celsius and convert it into Fahrenheit using formula (c * 9/5 + 32 = f).

def CelToFah(c):
    return (c * (9/5)) + 32
def FahToCel(f):
    return (f - 32) * (5/9)


def Choice():
    ch = int(input("Enter Temperature in Celsius (1) Or Fahrenheit (2) : "))
    if (ch == 1):
        cel = float(input("Enter Temperature in Celsius : "))
        print("\nTemperature in Fahrenheit is : ", CelToFah(cel))
    elif (ch == 2):
        fah = float(input("Enter Temperature in Fahrenheit : "))
        print("\nTemperature in Celsius is : ",FahToCel(fah))

Choice()