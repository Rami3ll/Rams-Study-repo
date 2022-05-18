#!/usr/bin/python3


# A program that determines a worker's pay and multiplies their pay by a value if they worked over 40hours
print("To calculate your pay fill in the following ")
rate = int(input("Enter the rate of pay: "))
hours = int(input("Enter your work hours: "))
if (hours > 40):
    print("Your pay is " + str(rate * hours / 1.5))
else:
    print("Your pay is " + str(rate * hours))

print()
print()

# A program that determines a workers pay and handles invalid input with try and except:
print("Hey there! fill the following info to calc your pay")
rate = input("Enter the rate of pay: ")
hours = input("Enter your work hours: ") 
try:
    rate = int(rate)
    hours = int(hours)
    print("Your pay is " , (rate * hours))
except:
    print("Invalid input :) I only accept numbers!")

print()
print()

# A program that prompts for a score btw 0.0 & 1.0 and if out of range prints an error message and else if in range prints a grade
print("Hey welcome to the grade calculator! fill the following to calculate your grades:")
score = float(input("Enter your score between 0.0 - 1.0: "))
try:
    if score >= 0.9:
        print("A")
        print("Awesome!")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
        print("Olodo *sigh")
except:
    print("Invalid input :) sorry I only take numerics.")
