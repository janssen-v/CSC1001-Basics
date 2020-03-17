# Question 1
# Approximate the square root

def sqrt(n):
    x = float(n)
    if x == 0:
        return 0
    lastGuess = x / 2
    nextGuess = (lastGuess + (x / lastGuess)) /2
    while abs(nextGuess - lastGuess) >= 0.001:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (x / lastGuess)) /2
    return nextGuess

print("The Square Root Calculator v1.0 RC4")
print()
print("Input a number n to be square rooted.")
n = input("n: ")
print("The square root of", n, "is", sqrt(n))

