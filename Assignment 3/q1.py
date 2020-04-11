class Flower:
    # Initializes instance variables (str, int, float)
    def __init__(self, name = 'flowername', petals = 0, price = 0.0):
        self.name = name
        self.petals = petals
        self.price = price
    
    # Method to set individual values of type
    def setName(self, newName):
        self.name = str(newName)
    def setPrice(self, newPrice):
        self.price = float(newPrice)
    def setPetals(self, newPetals):
        self.petals = int(newPetals)

    # I don't really understand what the question meant by retrieving the value of each type
    # since the value of e.g. type flower1 can be returned directly through flower1.name....
    # Therefore I defined these methods to print as well as return type values

    # Method to print and return individual values of a type
    def retName(self):
        print ('The name of the flower is:', self.name)
        return self.name
    def retPrice(self):
        print ('The price of the flower is:', self.price)
        return self.price
    def retPetals(self):
        print ('The amount of petals that the flower has is:', self.petals)
        return self.petals

    # Method to print and return all values of a type
    def attributes(self):
        name = self.name
        petals = self.petals
        price = self.price
        print ('The', name, 'flower has', petals, 'petals')
        print ('and costs', price, 'RMB')
    def retAttributes(self):
        name = self.name
        petals = self.petals
        price = self.price
        return (name, petals, price) # Returns values as a tuple


# Sample outputs from using the Flower() class

# Example class type "flower1"
flower1 = Flower()
# Setting values of a type with defined methods
flower1.setName("Rose")
flower1.setPetals(40)
flower1.setPrice(25.5)
# Printing type values individually
print()
print('Direct printing of individual type values:')
print()
print(flower1.name)
print(flower1.petals)
print(flower1.price)
# Printing all type values combined with method retAttributes
print()
print ('Combined printing of returned type values with retAttributes method:')
print()
print(flower1.retAttributes())

# Example class type "flower2"
flower2 = Flower("Crysanthemum", 5, 34.2)
# Printing type values individually with retValue method
print()
print('Direct printing of individual type values with the retValue Method:')
print()
flower2.retName()
flower2.retPrice()
flower2.retPetals()
# Printing all type values combined with method attributes
print()
print('Combined printing of type values with attributes method:')
print()
flower2.attributes()

