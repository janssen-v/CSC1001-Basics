# Locker Puzzle
def locker_puzzle(num):
    lockerState = [False]*num
# Starts on every next locker with every student, the increment
# of lockerstate changes increasing with student count as well.
    for students in range(1, num+1):
        for lock in range(students, num+1,students):
            lockerState[lock-1] = not lockerState[lock-1]  
    return lockerState

for state,open in enumerate(locker_puzzle(100)):
    if open:
        print('Locker', state+1) # Because starts from zero