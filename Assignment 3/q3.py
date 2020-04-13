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
            print('The Ecosystem is overpopulated, shutting down simulation.')
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
    riverLength = int(input('River length: '))
    bearAmount = int(input('Amount of Bears: '))
    fishAmount = int(input('Amount of Fish: '))
    nSimulations = int(input('Number of simulations: '))
    ecosystem = Ecosystem(riverLength, bearAmount, fishAmount, nSimulations)
    ecosystem.simulation(nSimulations)
    