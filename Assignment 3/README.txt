README - How to Run the Programs
Note: All programs written and tested on Python 3.6.7 64-Bit on Ubuntu Linux 18.04
If there are any issues with regards to program execution beyond the scope of this
guide, please direct any and all questions to 119010518@link.cuhk.edu.cn

Question 1 - Class to represent flower
The class can be initialized with Flower(Flowername, Number of Petals, Flower Price)
if no values are entered, it will default to an empty string for the flowername, and
zero values for both petals and price

It's callable methods are:

self.setName(newName) -> changes flower name
self.setPrice(newPrice) -> changes flower price
self.setPetals(newPetals) -> changes flower petal count
self.retName() -> prints and returns flower name
self.retPrice() -> prints and returns flower price
self.retPetals() -> prints and returns flower petal count
self.attributes() -> prints all attributes of the flower
self.retAttributes() -> returns all attributes of the flower 

They can be accessed through the class by importing the python file and calling them.

Example usage would be something like:
rose = Flower()
rose.setName('Rose')
rose.setPetals(40)
rose.setPrice(25.5)
print(rose.retAttributes())

Alternatively, run the program in a python terminal to see code sample outputs
these will not affect usage of the class if imported into another python program
because they run only if executed directly.

Question 2 - Differentiation Class

The class can be initialized with Differential(polynomial)
The polynomial should be similar to this form -> 2*x^3+3*x^2+5*x+1
No spaces, single variable only, prefix variable with * unless it doesn't have a coefficient

User can call the self.getDifferential() method to return the first derivative of the polynomial that was
used to initialize the class.

I have also wrote a main function to use the class directly for testing.
To run the program just follow the onscreen instructions on launch.

Question 3 - Ecosystem Simulator

Initialize the class with -> Ecosystem(riverLength, bearAmount, fishAmount)
All class methods are private except the self.simulation(method), which is the only one
intended to be called by the user.

Setting class values for simulation should always occur during class initialization
e.g. 
ecosystem = Ecosystem(10, 2, 3, 4)
simulations = ecosystem.simulation(nSimulations)

The method self.simulation(nSimulations) will return a list with the initial generated state
in the first index position and the rest of the simulations in order of procession.

ILLUSTRATION:
simulations = ecosystem.simulation(3)
simulations -> [initialState, simulation 1, simulation 2, simulation 3]

There is a sample program provided that demonstrates usage of the class
it can be run by running the q3.py python file directly in a python terminal
Just follow the onscreen instructions, it is straightforward.

I think one of the downsides of the current implementation is that because the simulation
is carried out per object left to right, while the ecosystem is immediately updated,
animals that are spawned from a simulation of a previous object will immediately be simulated
instead of waiting for the next simulation, which I think is more accurate.

But the specifications do not mention that :)