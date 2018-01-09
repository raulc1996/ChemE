"""01/09/2017
Temperature Calculator
Celsius
Kelvin
Fahrenheit
Rankine
"""
#Define initial unit
initial_unit = input("Enter initial temperature unit " + "c, k, f, r:")
while initial_unit != "c" and initial_unit != "k" and initial_unit != "f" and initial_unit != "r":
    initial_unit = input("incorrect unit, try again:")
if initial_unit == "c":
    cel = float(input("Degree celsius:"))
    kel = cel + 273.15
    fah = cel * 9/5 + 32
    ran = kel * 9/5
elif initial_unit == "k":
    kel = float(input("Kelvin:"))
    cel = kel - 273.15
    fah = kel * 9/5 - 459.67
    ran = kel * 9/5
elif initial_unit == "f":
    fah = float(input("Degree fahrenheit:"))
    cel = (fah - 32) * 5/9
    kel = (fah + 459.67) * 5/9
    ran = fah + 459.67
elif initial_unit == "r":
    ran = float(input("Degree Rankine:"))
    cel = (ran - 491.67) * 5/9
    kel = ran * 5/9
    fah = ran - 459.67

print(" ")
print("Celsius " + str(cel))
print("Kelvin " + str(kel))
print("Fahrenheit " + str(fah))
print("Rankine " + str(ran))