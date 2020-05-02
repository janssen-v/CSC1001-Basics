# Question 1 - Recursive Algorithm, Count

class Node(object):
    def __init__(self, data = None, nextNode = None):
      self.data = data # List head
      self.nextNode = nextNode

    def getNext(self):
        return self.nextNode

class linkedList:
    def __init__(self):
        self.head = None

    def add(self, newNext):
        newNode = Node(newNext)
        newNode.nextNode = self.head
        self.head = newNode

    # Better way to implement recursive count
    # e.g. list1.reCount vs reCount(list1) 

    # def count(self, head): # Count function
    #     if head:
    #         return 1 + self.count(head.getNext())
    #     else: return 0
    # def reCount(self): # Recursive count
    #         return self.count(self.head)

def count(head): # Count function
    if head:
        return 1 + count(head.getNext())
    else: return 0
def reCount(node): # Recursive count
    # check if node is linkedlist for robustness
    return count(node.head)

if __name__ == "__main__":
    list1 = linkedList()
    list1.add(0)
    list1.add(6)
    list1.add(2)
    list1.add(3)
    print(reCount(list1))
    
