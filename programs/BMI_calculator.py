#Bmi (Body,Mass,Index) measures the body fat based on height and weight.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight)/float(height)**2
bmi_as_int = int(bmi)
print (bmi_as_int)
