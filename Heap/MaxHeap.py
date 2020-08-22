class MaxHeap:
    def __init__(self, array):
        # this will store the array returned in form of heap
        self.heap = self.buildHeap(array)

    # this method creates the heap
    def buildHeap(self, array):
        # we'll consider the bottomup approach
        # this will store the parent of the last element or the last ParentNode
        firstParentIndex = len(array)-2 // 2

        # looping through all the parentNodes
        # we took reverse because we want to start from the last parentNode
        for currentIndex in reversed(range(firstParentIndex)):
            # calling shiftDown method for all the parentNodes
            # starting from the last parentNode
            self.shiftDown(currentIndex, len(array)-1, array)

        return array

    def shiftUp(self, currentIndex, heap):

        # finding the parentNOde of the newly inserted Node
        parentIndex = (currentIndex - 1) // 2

        # first condition - while it is not the root node
        # second - if the parent of the newly inserted node is smaller than the node itself
        # swap the two
        while parentIndex > 0 and heap[parentIndex] < heap[currentIndex]:
            self.swap(currentIndex, parentIndex, heap)
            # change the currentINdex as the newly inserted newly is shifted up now
            currentIndex = parentIndex

            # recalculate the parentNode of the currentNode as it is moved upwards
            parentIndex = (currentIndex-1) // 2

    def shiftDown(self, currentIndex, endIndex, heap):
        # getting the childOneNode of last parent
        childOneIndex = (currentIndex * 2)+1
        while childOneIndex <= endIndex:
            # if there's a childTwoNode then take it
            childTwoIndex = (currentIndex * 2) + 2 if currentIndex * 2 + 2 <= endIndex else -1

            # now checking which childNode is the bigger one
            if childTwoIndex != -1 and heap[childOneIndex] < heap[childTwoIndex]:
                idxToRemove = childTwoIndex
            else:
                idxToRemove = childOneIndex

            # if the childNode is bigger than the parentNode then swap the two
            if heap[currentIndex] < heap[idxToRemove]:
                # swap method thales three arguments
                # currentIndex is the index of the parentNode
                # other one is the childNode which is bigger than the parentNode
                self.swap(currentIndex, idxToRemove, heap)
                # after swapping make currentIndex equal to the new childNode
                currentIndex = idxToRemove
                # calculate child of that node
                childOneIndex = currentIndex * 2 + 1

            else:
                break

    def insert(self, value):
        # every time we insert an element, we add to the end of the heap then perform shiftUp
        self.heap.append(value)

        # this will keep shiftingUp the Node to its right position
        # currentIndex = index of the newly inserted node
        self.shiftUp(len(self.heap)-1, self.heap)

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        
        self.shiftDown(0, len(self.heap)-1, self.heap)

    def swap(self,i ,j, heap):
        heap[i], heap[j] = heap[j], heap[i]


# this is an unsorted array and we'll create a heap out of it
arr = [30, 12, 43, 54, 23, 4, 5, 41, 67]

# creating the max heap instance by passing the array
heap = MaxHeap(arr)
heap.buildHeap(arr)
# this will print the heapify array
print(arr)
