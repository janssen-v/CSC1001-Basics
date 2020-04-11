from random import random 
class Ecosystem:
    def __init__(self, riverLength = 0, bearAmount = 0 , fishAmount = 0, river = []):
        self.riverLength = riverLength
        self.bearAmount = bearAmount
        self.fishAmount = fishAmount
        self.river = river
        
    def randomizer(self):
        probability = random()
        if probability <= 0.5:
            return True
        else:
            return False

    def allocator(self):
        bearCount = self.bearAmount
        fishCount = self.fishAmount
        noneCount = self.riverLength - (bearCount + fishCount)
        while True:
            if bearCount > 0:
                river.append('B')
                bearCount -= 1
            elif fishCount > 0:
                river.append('F')
                fishCount -= 1
            elif noneCount > 0:
                river.append('N')
            else:
                self.river = random.shuffle(river)
                break

    def simulation(self):
        times = self.riverLength
        river = self.river
        for i in range(times):
            if 'B' in river[i] or 'F' in river[i]: # to check if location[i] in list is F B or N
                if randomizer():    # moves the object
                    if randomizer():
                        return 'Left'
                    else:
                        return 'Right'
                else:
                    return None

class River(Ecosystem):
    def __init__(self, riverLength=0, bearAmount=0, fishAmount=0, river=[]):
        super().__init__(riverLength=riverLength, bearAmount=bearAmount, fishAmount=fishAmount, river=river)

    def drawRiver(self):
        self.river = river

    def bearObj(self):
        representation = 'B'
        return representation
    
    def fishObj(self):
        representation = 'F'
        return representation

if __name__ == "__main__":
    while True:
        try:
            riverLength = input(int('River length: '))
            assert(riverLength > 0), 'riverLength must be bigger than 0'
            bearAmount = input(int('Amount of Bears: '))
            assert(bearAmount > 0), 'bearAmount must be bigger than 0'
            fishAmount = input(int('Amount of Fish: '))
            assert(fishAmount > 0), 'fishAmount must be bigger than 0'
            assert((fishAmount + bearAmount <= riverLength), 'Your ecosystem is overpopulated'
            break
        except ValueError:
            print('Please input a valid positive integer')
    
    ecosystem = Ecosystem(riverLength, bearAmount, fishAmount)
    ecosystem.allocator()
    pass