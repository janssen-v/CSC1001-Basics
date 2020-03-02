#Question 2

#Asks the user to input an integer
num = (input("Enter an integer: "))

#Header for vertical list
print ("The integer is: ")

#Converts input into a horizontal list
horz = list(num)

#This prints the list vertically
for i in range(len(horz)):
    print(horz[i], end ='''
''')