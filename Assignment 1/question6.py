# Question 6
# Given a trigonometric function f(x) and a real interval [a,b], integrate

import math

aInputOk = False
bInputOk = False
nInputOk = False
trigFunctionOk = False

print ("Input a trigonometric function")
print ("Options: sin, cos, tan")
trigFunction = input ("Function: ")
while trigFunction not in ("sin", "cos", "tan"):
    print ("ERROR. You can only choose from sin, cos, and tan")
    trigFunction = input ("Function: ")

print ("Input the interval end points [a, b]")
while not aInputOk:
    try:
        a = input ("End point a: ")
        a = float(a)
        aInputOk = True
    except ValueError:
        print ("ERROR. Plase input a valid endpoint.")

while not bInputOk:
    try:
        b = input ("End point b: ")
        b = float(b)
        bInputOk = True
    except ValueError:
        print ("ERROR. Plase input a valid endpoint.")

print ("Input the number of sub-intervals: ")
while not nInputOk:
    try:
        n = input ("Sub-intervals: ")
        n = int(n)
        nInputOk = True
    except ValueError:
        print ("ERROR. Plase input a valid integer value.")

while not trigFunctionOk:
    try:
        trigFunction in ("sin")
        trigFunction = math.sin(x)
        trigFunctionOk = True
    except trigFunction in ("cos"):
        trigfunction = math.cos(x)
        trigFunctionOk = True
    except trigFunction in ("tan"):
        trigfunction = math.tan(x)
        trigFunctionOk = True

for i in range (1, n):
    integral = ((b-a)/n) * trigFunction(a + ((b-a)/n) * (i-0.5))
    print (integral)