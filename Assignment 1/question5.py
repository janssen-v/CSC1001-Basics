# Question 5
# Find all primes smaller than input N99

prime = [] # Creates the prime list
inputok = False
while not inputok: # Foolproof input, repeats until integer is input
    try:
        n = input("Input an integer N: ") # Requests user input
        nstring = n # Preserves string format for printing header
        n = int(n)  # Converts string into integer, while checking input type
        inputok = True # Confirms input is an integer
    except ValueError: # Error upon non-integer input, loops back to input
        print("ERROR. Please enter an integer") 

 # A prime can only be divided by itself and 1
 # This function checks if a value can be divided by anything other than itself and 1
 # When it finds a number that can divide without remainder, it restarts the loop
 # When it finds no other divisors, it appends the number to the list of primes
for val in range(0, n + 1): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0:
               break
       else:
           prime.append(val)

# This print function references nstring as n has been converted into an int
# which sometimes gives inaccurate results when printing.
print("The prime numbers smaller than", nstring, "include: ")

# Prints 8 primes per line
start=0
while (start<len(prime)):
    end = start + 8 # Defines the end of the range as a distance of 8 items from [start]
    output = prime[start:end] # Defines output as a range of primes from [start] to [end]
    print(*output, ' ') # The star removes the brackets from the list
    start = end # Moves the start of the next output range to the end of the previous