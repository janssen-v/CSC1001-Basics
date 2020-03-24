# Locker Puzzle
lockerState = [False]*100
# Starts on every next locker with every student, the increment
# of lockerstate changes increasing with student count as well.
for students in range(1, 101):
    for lock in range(students, 101,students):
        lockerState[lock-1] = not lockerState[lock-1]  

for state,open in enumerate(lockerState):
    if open:
        print('Locker', state+1) # Because starts from zero