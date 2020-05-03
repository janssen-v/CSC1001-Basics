# Question 2 - Quick sort over singly linked list

class Node(object):
    def __init__(self, data = None, nextNode = None):
      self.data = data # List head
      self.nextNode = nextNode

    def getNext(self):
        return self.nextNode

    def nextExists(self):
        if self.getNext() != None:
            return True
        elif self.getNext() == None:
            return False
    
    def getData(self):
        return self.data
    
    def setNext(self, newNext):
        self.nextNode = newNext

class linkedList:
    def __init__(self):
        self.head = None

    def add(self, data):        # Adds from outside of list
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def addNode(self, node):    # Adds from inside of list
        node.setNext(self.head)
        self.head = node
    
    def count(self, head):  # Count function
        if head:
            return 1 + self.count(head.getNext())
        else: return 0

    def reCount(self):      # Count recursion
            return self.count(self.head)

    def sort(self): # The quick sort
        if self.reCount() > 1:
            tempStore = []
            now = self.head
            tempStore.append(self.head)
            while now.nextExists():
                now = now.getNext()
                tempStore.append(now)
            tempStore = sorted(tempStore, key = lambda node: node.getData(), reverse = True)  # True for ascending sort
            sortStore = linkedList()                                                          # False for descending sort  
            for node in tempStore:                                                            # Because the list is reversed
                sortStore.addNode(node)
            return sortStore
        return self

    def listPrint(self):    # Function to print entire list, for convenience
        if self.head is None:
            return
        now = self.head
        print(str(now.getData()))
        while now.nextExists():
            now = now.getNext()
            print(str(now.getData()))

if __name__ == "__main__":
    unsorted = linkedList()
    unsorted.add(0)
    unsorted.add(7)
    unsorted.add(4)
    unsorted.add(9)
    unsorted.add(3)
    print('UNSORTED')
    unsorted.listPrint()
    print('SORTED')
    isSorted = unsorted.sort()
    isSorted.listPrint()