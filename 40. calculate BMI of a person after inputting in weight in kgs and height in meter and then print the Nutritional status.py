weight_in_kg=float(input("Enter Weight in kg :"))
height_in_meter=float(input("Enter Height in meter :"))
bmi=weight_in_kg/(height_in_meter*height_in_meter)
print("BMI is :",bmi,end=" ")
if bmi<18.5:
    print("...Underweight")
elif bmi<25:
    print("...Normal")

elif bmi<30:
    print("...Overweight")
else:
    print("...Obese")