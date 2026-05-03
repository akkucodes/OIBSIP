print("BMI Calculator")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
# basic validation
if weight <= 0 or height <= 0:
    print("Weight and height must be positive values.")
else:
    # small check for wrong unit input
    if height > 2.2:
        print("Height looks incorrect. Please enter in meters (example: 1.7)")
    else:
        bmi = weight / (height * height)
        print("\nYour BMI is:", round(bmi, 2))
        # deciding category
        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")
