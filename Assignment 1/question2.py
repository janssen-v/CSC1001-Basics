#Question 2

#Asks the user to input an integer
num = (input("Enter an integer: "))
#Checks if input is an integer
try:
    val = int(num)
    #Converts input into a list
    horz = list(num)
    #Header for vertical list
    print ("The integer is: ")
    #Prints list vertically
    for i in range(len(horz)):
        print(horz[i], end ='''
''')
except ValueError:
    print("You did not input an integer, please try again")











