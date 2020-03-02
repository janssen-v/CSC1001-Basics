#Question 2 - Display integer input in a vertical list

done = False
#Loops statements until integer is input
while not done:
    try:
        #Asks the user to input an integer
        num = (input("Enter an integer: "))
        #Checks if input is an integer
        int(num)
        #Converts input into a list
        horz = list(num)
        #Header for vertical list
        print ("The integer is: ")
        #Prints list vertically
        for i in range(len(horz)):
           print(horz[i], end ='''
''')
        #Marks program as complete
        done = True
    #Repeat on failure
    except ValueError:
        print("You did not input an integer, please try again")











