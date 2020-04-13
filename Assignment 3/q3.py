import random
class Ecosystem:
    def __init__(self, riverLength = 0, bearAmount = 0 , fishAmount = 0, nSimulations = 0):
        self.riverLength = riverLength
        self.bearAmount = bearAmount
        self.fishAmount = fishAmount
        self.bear = 'B'
        self.fish = 'F'
        self.none = 'N'
        self.river = []
    
    # Generator Methods
    def randomizer(self):
        roll = random()
        if roll <= 0.5:
            return True
        else:
            return False

    def allocator(self):
        bearCount = self.bearAmount
        fishCount = self.fishAmount
        river     = self.river
        noneCount = self.riverLength - (bearCount + fishCount)
        while True:
            if bearCount > 0:
                river.append(self.bear)
                bearCount -= 1
            elif fishCount > 0:
                river.append(self.fish)
                fishCount -= 1
            elif noneCount > 0:
                river.append(self.none)
            else:
                self.river = random.shuffle(river)
                break

    def generate(self, create): # generates the create object at random empty position
        indices = [i for i, x in enumerate(self.river) if x == self.none]
        position = random.choice(indices)
        self.river[position] = create

    # Behaviour and Collision Models
    def bearObj(self, meet, origin, destination):
        if meet == self.bear:
            self.generate(self.bear)
            self.bearAmount += 1 # increases record of bear by 1
        elif meet == self.fish:
            self.fishAmount -= 1 # subtracts record of fish by 1
            self.river[destination] = self.bear
            self.river[origin] = self.none
    
    def fishObj(self, meet, origin, destination):
        if meet == self.bear:
            self.river[origin] = self.none
            self.fishAmount -= 1 # subtracts record of fish by 1
        elif meet == self.fish:
            self.generate(self.fish)
            self.fishAmount += 1 # increases record of fish by 1

    def collision(self, origin, vector):
        destination = origin + vector
        originObj = self.river[origin]
        destinationObj = self.river[destination]
        if originObj == self.bear:
            self.bearObj(destinationObj, origin, destination)
        elif originObj == self.fish:
            self.fishObj(destinationObj, origin, destination)

    def simulation(self, nSimulations):
        self.allocator()
        riverPart = range(self.riverLength)
        for i in range(nSimulations):
            for i in riverPart:
                if self.bear in self.river[i] or self.fish in self.river[i]: # to check if location[i] in list is F B or N
                    if self.randomizer():    # moves the object
                        if self.randomizer():
                            direction = -1 # move left
                        else:
                            direction = 1 # move right
                    collision(i, direction)
                    print (''.join(self.river))

if __name__ == "__main__":
    riverLength = int(input('River length: '))
    bearAmount = int(input('Amount of Bears: '))
    fishAmount = int(input('Amount of Fish: '))
    nSimulations = int(input('Number of simulations: '))
    ecosystem = Ecosystem(riverLength, bearAmount, fishAmount, nSimulations)
    ecosystem.simulation(nSimulations)
    