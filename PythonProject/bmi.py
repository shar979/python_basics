
# bmi calc
# Underweight:Below 18.5
# Healthy Weight:18.5-24.9
# Overweight: 25.0-29.9
# Obesity (Class I):30.0-34.9
# Obesity (Class II):35.0-39.9
# Severe Obesity (Class III): 40.0/higher

weight =input("Please enter your weight in Kilograms: ")
height= input("Please enter your height in metres: ")

w = float(weight)
h = float(height)
bmi = w / h**2
# 10**3 math.pow(h,2) h*h

if bmi<18.5:
    print("you are underweight")
elif  18.5 <= bmi <=24.9:
    print("You are healthy")
elif      bmi>=25 and bmi<=30:
    print("You are overweight")
elif 30 <= bmi <=34.9:
    print("You are obese class 1")
elif  35 <= bmi <=39.9:
    print("You are obese class 2")
else:
        print("You are obese class 3")