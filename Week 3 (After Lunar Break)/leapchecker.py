# Leapchecker

def isLeapYear(year):
    try:
        year % 4 == 0
        year % 100 == 0
        year % 400 == 0
        print(year, "is leap")
    else:
        print(year, "is not leap")

year = int(input())
isLeapYear(year)