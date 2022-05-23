#!/usr/bin/python3
# The purpose of the def keyword has two functions ; to indicate the start of a function & The indented sequence of statements are to be stored for later use when the defined function is called.

# The program would print ABC ZAP ABC accordingly in the order in which the functions were called.

# Pay computation program with a user defined function 
def computepay(hours, rate) :
        result = hours * rate
        return result

try:
    hours = float(input("Enter your work hours: "))
    rate = float(input("Enter your work rate "))
    pay = computepay(hours, rate)
    print(pay)
except:
    print("Hey I only accept numerics :)")

print()
print()

print("An Alternative method")
hours = input("Enter your work hours: ")
rate = input("Enter your work rate: ")
def computepay(hours, rate) :
    try:
        hours = float(hours)
        rate = float(rate)
        result = hours * rate
        return result
    except:
        print("Hey I only accept numerics :)")

pay = computepay(hours, rate)
print(pay)


print()
print()

# Grade computation program with user defined functions:
score = input("Enter your score: ")
def computegrade(score) :
    try:
        score = float(score)
        if score >= 0.9 and score <= 1  :
            print("A")
            print("Awesome!")
        elif score > 1.0:
            print("Please enter a score between 0.0 - 1.0")
        elif 0.8 >= score < 0.9:
            print("B")
        elif 0.7 >= score < 0.8:
            print("C")
        elif 0.6 >= score < 0.7:
            print("D")
        elif score < 0.6:
            print("F")
            print("Olodo *sigh")
    except:
        print("Invalid input :) sorry I only take numerics.")
        return score
computegrade(score)
