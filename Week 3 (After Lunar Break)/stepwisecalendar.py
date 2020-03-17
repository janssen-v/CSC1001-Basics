## Print Calendar example
# Enter a year, and a month to display a calendar given that January 1 1800 is Wednesday
# Tell the difference between Leap Year and non-Leap Year
# Identify first and last day to print
# Make Flowchart of what to do

def isLeap(year):
    try:
        year % 4 == 0
        year % 100 == 0
        year % 400 == 0
        print(year, "is leap")
    else:
        print(year, "is not leap")