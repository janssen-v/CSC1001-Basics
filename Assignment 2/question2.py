# Question 2
# Display the Emirps
# Program Flow
# 0. Enumerator
# 1. Check if Palindrome
# 2. Check if Prime
# 3. If Prime && Palindrome, add to list
# 4. When list has 100 items, print

palinPrime = []
candidatePrime = 1
totalFound = 0

# Checks if palindrome
def isPalindrome(num):
    num = list(str(num)) # int not iterable
    num = list(map(int, num))
    if num == num[::-1]:
        return True

# Checks if prime
def isPrime(num):
    if num > 1: 
        for n in range(2, num): 
            if (num % n) == 0:
                break
        else:
            return True

print('Please wait while we compute your primes.')
print()

while totalFound < 100:
    candidatePrime += 1
    if isPrime(candidatePrime) and isPalindrome(candidatePrime):
        totalFound += 1
        palinPrime.append(candidatePrime)
else:
    # Splits list into more lists to display per row
    palinPrime = [palinPrime[i:i+10] for i in range(0, len(palinPrime), 10)]
    for primes in palinPrime:
        print('{:>8} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8}'.format(*primes))
    print()
    print('Complete.')
