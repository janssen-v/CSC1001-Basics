# Question 2 - Quick sort over singly linked list

# Quick sort function
def part(arr, start, end): # Quick sort partition
    pivot = start
    for i in range(start+1, end+1):
        if arr[i] <= arr[start]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]     # At first, I actually thought of storing the values of arr[pivot] and arr[i] inside temporary variables
    arr[pivot], arr[start] = arr[start], arr[pivot]     # But on second thought, that would create new memory values, which is counter to the point of an in place sort
    return pivot                                        # I found out that the values can be swapped in this fashion only recently after seeing an example on the internet

def qSort(arr, start, end): # Quick sort function
    if start >= end:
        return
    pivot = part(arr, start, end)
    qSort(arr, start, pivot-1)
    qSort(arr, pivot+1, end)

def qSortRec(arr):   # Quick sort function recursion
    start = 0
    end = len(arr)-1
    return qSort(arr, start, end)


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
    
    def count(self, head):  # Count function
        if head:
            return 1 + self.count(head.getNext())
        else: return 0

    def reCount(self):      # Count recursion
            return self.count(self.head)   

    def sort(self): # Quicksort a linked list. Personally I think merge sort is better suited for linked lists.
        if self.reCount() > 1:
            tempStore = []
            now = self.head
            tempStore.append(now.getData())
            while now.nextExists():
                now = now.getNext()
                tempStore.append(now.getData())
            # quicksort tempstore
            qSortRec(tempStore)
            tempStore.reverse() # Reverses the order, because it is descending initially, and ascending is wanted
            sortStore = linkedList()                                                            
            for node in tempStore:                                                            
                sortStore.add(node)
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