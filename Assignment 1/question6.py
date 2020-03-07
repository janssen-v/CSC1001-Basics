# Question 6
# Given a trigonometric function f(x) and a real interval [a,b], integrate

import math # I imported the entire math library out of habit

aInputOk = False
bInputOk = False
nInputOk = False
trigFunctionOk = False
integral = 0

print ("Input a trigonometric function")
print ("Options: sin, cos, tan")
trigFunction = input ("Function: ")

# This rejects input that is not sin, cos, and tan
# Case sensitive, and only accepts lower case inputs
# There was a way I found on Google to accept random case but it required installing a custom library
# Can't think of any other (simple) way to do so. If there are any suggestions, let me know.

while trigFunction not in ("sin", "cos", "tan"):
    print ("ERROR. You can only choose from sin, cos, and tan")
    trigFunction = input ("Function: ")

print ("Input the interval end points [a, b]")
while not aInputOk:
    try:
        a = input ("End point a: ")
        a = float(a) # I used a float in this scenario because the intervals might not be fixed integer values
        aInputOk = True
    except ValueError: # Rejects non numerical inputs, such as strings
        print ("ERROR. Plase input a valid endpoint.")

while not bInputOk: # Maybe next time I should just define the function to make it less cluttered
    try:
        b = input ("End point b: ")
        b = float(b) # Same as before in a
        bInputOk = True
    except ValueError: # Same as before in a
        print ("ERROR. Plase input a valid endpoint.")

print ("Input the number of sub-intervals: ")
while not nInputOk: # This loop accepts input while making sure it is of the correct class
    try:
        n = input ("Sub-intervals: ")
        n = int(n) # The input for this has to be an integer, as specified in the assignment sheet
        nInputOk = True
    except ValueError:  # Same as before in a
        print ("ERROR. Plase input a valid integer value.")

# Checks the function to be integrated from the first input and executes the integration algorithm provided in the assignment sheet
# I am aware that there is a better way to do this, but this was the first (and easiest) that came to mind.
# Furthermore, any improvements would not improve program performance by much, perhaps only saving some lines of code and improving readability.
# This is because Python is an high-level interpreted language, that already comes with performance penalties

while trigFunction in ("sin"):
    for i in range (1, n+1):   
        integral += ((b-a)/n) * math.sin((a + ((b-a)/n) * (i-0.5))) # The function here is math.sin instead of just sin because I imported the entire math library
    break                                                           # instead of using from math import sin and etc, same results either way. Also better coding practice.
while trigFunction in ("cos"):
    for i in range (1, n+1):
        integral += ((b-a)/n) * math.cos((a + ((b-a)/n) * (i-0.5)))
    break
while trigFunction in ("tan"):
    for i in range (1, n+1):
        integral += ((b-a)/n) * math.tan(a + ((b-a)/n) * (i-0.5))
    break

print ("The integration of", trigFunction,"(x)", "from", a, "to", b, "is", integral)