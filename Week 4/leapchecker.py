# Leapchecker

def isLeap(year):
    try:
        year % 4 == 0
        year % 100 == 0
        year % 400 == 0
        print(year, "is leap")
    else:
        print(year, "is not leap")