# Conditions

print(" ***************** Conditions *******************\n")

print("************* IF-Else Statement ******************\n")
num1 = 40
num2 = 30

if num1 > num2:
    print("Num1 is greater than Num2\n")
else:
    print("Num2 is greater than Num1\n")

print("************* IF-ElseIF Statement ******************\n")

if num1 > num2:
    print("Num1 is greater than Num2\n")
elif num2 == num1:
    print("Both Number Are Equal\n")

print("************* Nested IF-ElseIF Statement ******************\n")


if num1 > num2:
    if num1 == num2:
        print("Both Number Are Equal\n")
    else:
        print("Num1 is greater than Num2\n")
else:
    print("Num2 is greater than Num1\n")

