def bmi_report(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 1)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi <= 24.9:
        category =  "Normal weight"
    elif bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"      
        
    return(f"BMI: {bmi}, Category: {category}")            
    # TODO: calculate bmi, round it to 1 decimal place, determine the category,
    # and return "BMI: {bmi}, Category: {category}"
    pass