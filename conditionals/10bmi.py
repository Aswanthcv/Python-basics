'''Write a program that interprets the Body Mass Index (BMI) based on a user’s weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
• Under 18.5 they are underweight
• Over 18.5 but below 25 they have a normal weight
• Over 25 but below 30 they are slightly overweight
• Over 30 but below 35 they are obese
• Above 35 they are clinically obese.
'''

hight=float(input("Enter height in Meter: "))
weight=float(input("Enter weight in kg: "))
bmi=weight / (hight ** 2)
print(f"Your BMI is {bmi:.2f}")
if bmi <18.5:
    print("Underweight")
elif 18.5<bmi<=25:
    print("Normal") 
elif 25<bmi<30:
    print("Slightly overweight")
elif 30<=bmi<35:
    print("Obese")           
else:
    print("clinically obese")    