#Question 4

col1 = 0
done = False
while not done: # Repeats the program until positive integer input
    n = (input("Enter number N here: "))
    try:
        n=int(n) # Checks for numeric input, while converting it from a string to an integer
        print("m m+1 m**(m+1)") # Column Headers
        while n>0: # Checks for positive integer input
            while col1<=n: # Runs program until m (col1) progresses to n
                col1 += 1
                col2 = col1+1
                col3 = col1**col2
                dataset = [[col1, col2, col3]]
                for i in range(len(dataset)):
                    for j in range(len(dataset[i])):
                        print(dataset[i][j], end='  ')
                    print()
                done = True
        else: # Error for non-positive integer input
            print("ERROR. Please input a positive integer")
    except ValueError: # Error for non-numeric input
        print("ERROR. Please input a positive integer")