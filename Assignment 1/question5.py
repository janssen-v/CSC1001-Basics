# Question 5
# Prime number finder
p = []

inputok = False
while not inputok:
    try:
        n = input("Input an integer N: ")
        n = int(n)
        inputok = True
    except ValueError:
        print("ERROR. Please enter an integer")

for val in range(0, n + 1): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else:
           p.append(val)

print("The prime numbers smaller than 10 include:")
print(*p)