import random
class Ecosystem:
    def __init__(self, riverLength = 0, bearAmount = 0 , fishAmount = 0):
        self.__riverLength = riverLength
        self.__bearAmount = bearAmount
        self.__fishAmount = fishAmount
        self.__bear = 'B'
        self.__fish = 'F'
        self.__none = 'N'
    
    # Generator Methods
    def __randomizer(self):
        roll = random.random()
        if roll <= 0.5:
            return True
        else:
            return False

    def __allocator(self):
        bearCount = self.__bearAmount
        fishCount = self.__fishAmount
        noneCount = self.__riverLength - (bearCount + fishCount)
        river     = []
        while True:
            if bearCount > 0:
                river.append(self.__bear)
                bearCount -= 1
            elif fishCount > 0:
                river.append(self.__fish)
                fishCount -= 1
            elif noneCount > 0:
                river.append(self.__none)
                noneCount -= 1
            else:
                return river
                break

    def __generate(self, create, river): # generates the create object at random empty position
        emptyIndices = [i for i, x in enumerate(river) if x == self.__none]
        if emptyIndices == []:
            print('THE ECOSYSTEM IS OVERPOPULATED. NO MORE ANIMALS CAN SPAWN.')
        else:
            position = random.choice(emptyIndices)
            river[position] = create

    # Behaviour and Collision Models
    def __collision(self, origin, vector, river): # Collision director
        destination = origin + vector
        originObj = river[origin]
        destinationObj = river[destination]
        if destination >= 0 and destination <= (len(river)-1): # So that collision cannot go out of bounds
            if originObj == self.__bear:
                self.__bearObj(destinationObj, origin, destination, river)
            elif originObj == self.__fish:
                self.__fishObj(destinationObj, origin, destination, river)
    
    def __bearObj(self, meet, origin, destination, river):
        if meet == self.__bear:
            self.__generate(self.__bear, river)
        elif meet == self.__fish:
            river[destination] = self.__bear
            river[origin] = self.__none
        elif meet == self.__none:
            river[destination] = self.__bear
            river[origin] = self.__none
    
    def __fishObj(self, meet, origin, destination, river):
        if meet == self.__bear:
            river[origin] = self.__none
        elif meet == self.__fish:
            self.__generate(self.__fish, river)
        elif meet == self.__none:
            river[destination] = self.__fish
            river[origin] = self.__none

    # Main simulation logic control
    def simulation(self, nSimulations):
        river = self.__allocator()
        simulations = []
        simulations.append(''.join(river)) # -> append the initial state to list of simulations
        riverPart = range(self.__riverLength)
        for i in range(nSimulations):
            for j in riverPart:
                if self.__bear in river[j] or self.__fish in river[j]: # to check if location[i] in list is F B or N
                    if self.__randomizer():    # moves the object
                        if self.__randomizer():
                            direction = -1 # move left
                        else:
                            direction = 1 # move right
                        self.__collision(i, direction, river)
            simulations.append(''.join(river))
        return simulations # returns the simulations with the initial state as a list

if __name__ == "__main__":
    while True:
        try:
            print()
            print('ECOSYSTEM SIMULATOR by Vincentius Janssen')
            print()
            print('INSTRUCTIONS')
            print('1. Please enter the simulation parameters in positive integers.')
            print('2. If an input is detected as invalid, the program will restart.')
            print('3. The simulation will end when N number of simulations has elapsed, or if the river becomes overpopulated.')
            print('4. Please note that your river must be large enough to handle the initial amount of animals.')
            print()
            print('SIMULATION PARAMETERS')
            riverLength = int(input('River length (At least 1 units long): '))
            assert(riverLength > 0)
            bearAmount = int(input('Amount of Bears (Must be zero or more): '))
            assert(bearAmount >= 0)
            fishAmount = int(input('Amount of Fish (Must be zero or more): '))
            assert(fishAmount >= 0)
            assert(fishAmount + bearAmount <= riverLength)
            nSimulations = int(input('Number of simulations (At least one simulation): '))
            assert(nSimulations > 0)
            if nSimulations > 0:
                break
        except AssertionError:
            print('INVALID PARAMETER INPUT. PLEASE TRY AGAIN.')
            continue
        except ValueError:
            print('PLEASE INPUT A VALID POSITIVE INTEGER.')
        
    ecosystem = Ecosystem(riverLength, bearAmount, fishAmount)
    simulations = ecosystem.simulation(nSimulations)
    print()
    print('INITAL STATE BEFORE SIMULATION')
    print(simulations[0]) # Prints inital state before simulation begins
    del simulations[0] # Removes initial state from list of simulations
    print('SIMULATION OUTPUT FOR', nSimulations, 'SIMULATIONS.')
    for simulation in range(len(simulations)): # Prints simulations
        print(simulations[simulation]) 
    