# Question 3 - Tower of Hanoi (Iterative)
# Note: It is much easier to do the Tower of Hanoi with recursion

def move (origin, dest): # Move from origin to destination
    dest.insert(0, origin.pop(0))

def legalMove(tower1, tower2, name1, name2):
    if len(tower2) == 0 and len(tower1) != 0:   # Tower 2 is empty and tower 1 is not
        move(tower1, tower2)
        print(name1, '-->', name2)
    elif len(tower1) == 0 and len(tower2) != 0: # Tower 1 is empty and tower 2 is not
        move(tower2, tower1)
        print(name2, '-->', name1)
    elif len(tower1) >=0 and len(tower2) >= 0:  # Both towers have a disc inside
        if tower1[0] > tower2[0]:
            move(tower2, tower1)
            print(name2, '-->', name1)
        elif tower2[0] > tower1[0]:
            move(tower1, tower2)
            print(name1, '-->', name2)

def HanoiTower(n):
    towA = []
    towB = []
    towC = []
    towA.extend(range(1, n+1))
    
    if n%2 == 0: # EVEN
        while True:
            # Move AB
            try: legalMove(towA, towB, 'A', 'B')    # instead of adding try except for each move, a check function
            except: break                           # could have been used nested inside legalMove(), but that would
            # Move AC                               # require passing more parameters, which I wanted to avoid doing.
            try: legalMove(towA, towC, 'A', 'C')    # Plus, this came to mind the earliest.
            except: break
            # Move BC
            try: legalMove(towB, towC, 'B', 'C')
            except: break
                
    elif n%2 != 0: # ODD      
        while True:    
            # Move AC
            try: legalMove(towA, towC, 'A', 'C')
            except: break     
            # Move AB
            try: legalMove(towA, towB, 'A', 'B')
            except: break
            # Move BC
            try: legalMove(towB, towC, 'B', 'C')
            except: break
                
if __name__ == "__main__":
    print('Welcome to the TOWER OF HANOI SOLUTION PRINTER')
    while True:
        try:
            n = int(input('Please input n amount of disks to calculate for: '))
            assert n > 0
        except ValueError:
            print('Sorry, n must be an integer')
        except AssertionError:
            print("Sorry, I should've said that n must also be greater than 0")
        else:
            break
    HanoiTower(n)