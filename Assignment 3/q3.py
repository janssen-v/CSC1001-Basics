import random
class Ecosystem:
    def __init__(self, riverLength = 0, bearAmount = 0 , fishAmount = 0, nSimulations = 0):
        self.riverLength = riverLength
        self.bearAmount = bearAmount
        self.fishAmount = fishAmount
        self.bear = 'B'
        self.fish = 'F'
        self.none = 'N'
    
    # Generator Methods
    def randomizer(self):
        roll = random.random()
        if roll <= 0.5:
            return True
        else:
            return False

    def allocator(self):
        bearCount = self.bearAmount
        fishCount = self.fishAmount
        noneCount = self.riverLength - (bearCount + fishCount)
        river     = []
        while True:
            if bearCount > 0:
                river.append(self.bear)
                bearCount -= 1
            elif fishCount > 0:
                river.append(self.fish)
                fishCount -= 1
            elif noneCount > 0:
                river.append(self.none)
                noneCount -= 1
            else:
                return river
                break

    def generate(self, create, river): # generates the create object at random empty position
        emptyIndices = [i for i, x in enumerate(river) if x == self.none]
        if emptyIndices == []:
            print('THE ECOSYSTEM IS OVERPOPULATED. SHUTTING DOWN SIMULATION. HAVE A NICE DAY.')
            exit()
        position = random.choice(emptyIndices)
        river[position] = create

    # Behaviour and Collision Models
    def bearObj(self, meet, origin, destination, river):
        if meet == self.bear:
            self.generate(self.bear, river)
        elif meet == self.fish:
            river[destination] = self.bear
            river[origin] = self.none
        elif meet == self.none:
            river[destination] = self.bear
            river[origin] = self.none
    
    def fishObj(self, meet, origin, destination, river):
        if meet == self.bear:
            river[origin] = self.none
        elif meet == self.fish:
            self.generate(self.fish, river)
        elif meet == self.none:
            river[destination] = self.fish
            river[origin] = self.none

    def collision(self, origin, vector, river):
        destination = origin + vector
        originObj = river[origin]
        destinationObj = river[destination]
        if destination >= 0 and destination <= (len(river)-1): # So that collision cannot go out of bounds
            if originObj == self.bear:
                self.bearObj(destinationObj, origin, destination, river)
            elif originObj == self.fish:
                self.fishObj(destinationObj, origin, destination, river)

    def simulation(self, nSimulations):
        river = self.allocator()
        riverPart = range(self.riverLength)
        for i in range(nSimulations):
            for j in riverPart:
                if self.bear in river[j] or self.fish in river[j]: # to check if location[i] in list is F B or N
                    if self.randomizer():    # moves the object
                        if self.randomizer():
                            direction = -1 # move left
                        else:
                            direction = 1 # move right
                        self.collision(i, direction, river)
            print (''.join(river))

if __name__ == "__main__":
    while True:
        try:
            print()
            print('ECOSYSTEM SIMULATOR V1 by Vincentius Janssen')
            print()
            print('INSTRUCTIONS')
            print('1. Please enter the simulation parameters in positive integers.')
            print('2. If an input is detected as invalid, the program will restart.')
            print('3. Please note that your river must be large enough to handle the initial amount of animals.')
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
        
    ecosystem = Ecosystem(riverLength, bearAmount, fishAmount, nSimulations)
    print()
    print('SIMULATION OUTPUT FOR', nSimulations, 'SIMULATIONS.')
    ecosystem.simulation(nSimulations)
    