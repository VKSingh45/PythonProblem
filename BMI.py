# Program to calculate BMI (Body Mass Index) of a Person. Body Mass Index is a sample calculation using a 
# person's height and weight. The formula is BMI = kg/m^2 where kg is a person's weight in kilograms and m^2
# is their height in meter squares.

def BMI(w,h):
    return w/(h*h)
w = float(input("Enter Weight in Kilograms : "))
h = float(input("Enter height in meter : "))
print("BMI is : ", BMI(w,h))