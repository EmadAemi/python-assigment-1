weight = int(input("Weight(Kg): "))
height = int(input("Height(cm): "))
bmi = weight / ((height/100)**2)
if bmi<18.5:
    print("UNDERWEIGHT")
elif bmi<24.9:
    print("NORMAL")
elif bmi<29.9:
    print("OVERWEIGHT")
elif bmi<34.9:
    print("OBESE")
else:
    print("EXTREMELY OBESE")