# Week 2 Class 2
# No need to define datatypes in Python, will automatically do for you
# Use all caps to define a variable-constant. E.g. SEC_PER_MIN = 60
# Always define a variable-constant and use it, do not do direct calculations
# Input function returns a string always

# Practice -> Write a program to read a user's weight and height and then output his BMI

# BMI Calculator
h = float(input("input height here (m): "))
w = float(input("input weight here (kg): "))
bmi = (w / pow(h,2))

if bmi < 18.5:
    print("You are underweight with a BMI of", bmi)
elif 18.5 <= bmi <= 25.0:
    print("You are of normal weight with a BMI of", bmi)
elif 18.5 <= bmi <= 25.0:
    print("You are overweight with a BMI of", bmi)
elif 18.5 <= bmi <= 25.0:
    print("You are obese with a BMI of", bmi)

# Concatenation
# The operators + and * apply to strings
# + is for single concatenation, * is for multople concatenation
# Python will understand automatically

# Practice 2 -> Write program to generate a message to two friends with a stock template

# Eval function
# eval() takes a string and evaluates it as an expression just as if the programmer had directly entered the expression as code
# eval() returns the result of that expression, gives flexibility to determine what to execute at runtime
