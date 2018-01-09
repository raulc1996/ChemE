"""01/09/2017
Temperature Calculator
Celsius
Kelvin
Fahrenheit
Rankine
"""
#Define initial unit
initial_unit = raw_input("Enter initial temperature unit " + "c, k, f, r:")
while initial_unit != "c" and initial_unit != "k" and initial_unit != "f" and initial_unit != "r":
    initial_unit = raw_input("incorrect unit, try again:")
if initial_unit == "c":
    cel = input("Degree celsius:")
    kel = cel + 273.15
    fah = float(cel * 9/5 + 32)
    ran = float(kel * 9/5)
elif initial_unit == "k":
    kel = input("Kelvin:")
    cel = kel - 273.15
    fah = float(kel * 9/5 - 459.67)
    ran = float(kel * 9/5)
elif initial_unit == "f":
    fah = input("Degree fahrenheit:")
    cel = float((fah - 32) * 5/9)
    kel = float((fah + 459.67) * 5/9)
    ran = fah + 459.67
elif initial_unit == "r":
    ran = input("Degree Rankine:")
    cel = float((ran - 491.67) * 5/9)
    kel = float(ran * 5/9)
    fah = ran - 459.67

print " "
print "Celsius " + str(cel)
print "Kelvin " + str(kel)
print "Fahrenheit " + str(fah)
print "Rankine " + str(ran)