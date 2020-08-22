class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # you are given the most unsorted array of the world
        # and you build a heap out of it
        # we're going to grab the final node in the array and find its parentNode

        firstParentIdx = len(array) - 2 // 2

        # we've the last parent of the array
        for currentIndex in reversed(range(firstParentIdx)):
            self.shiftDown(currentIndex, len(array) - 1, array)

    def shiftUp(self, currentIndex, heap):
        # double slashes round the value
        # here we are getiing the index of the parent of the
        # newly inserted node

        parentIdx = (currentIndex - 1) // 2

        # first condition restricts from going above the root node
        # and other one checks if the currentNode is smaller than the parentNode

        while currentIndex > 0 and heap[currentIndex] < heap[parentIdx]:
            self.swap(currentIndex, parentIdx, heap)

            # after shifting up we have to update our currentNodeINdex as our node
            # has Shiftd Up

            currentIndex = parentIdx

            # similarly we have to update our parentNode as well
            parentIdx = (currentIndex - 1) // 2

    def shiftDown(self, currentIndex, endIndex, heap):

        childOneIndex = (currentIndex * 2) + 1

        while childOneIndex <= endIndex:
            # now we'll find the index of the second child if there is one
            childTwoIndex = (currentIndex * 2) + 2 if currentIndex * 2 + 2 <= endIndex else -1

            if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
                idxToRemove = childTwoIndex
            else:
                idxToRemove = childOneIndex

            if heap[idxToRemove] < heap[currentIndex]:
                self.swap(currentIndex, idxToRemove, heap)
                currentIndex = idxToRemove
                childOneIndex = currentIndex * 2 + 1

            else:
                break

    def insert(self, value):
        # every node that we insert is appended to the end of the heap
        self.heap.append(value)

        # then we shiftUp the value to it's right position
        # shiftUp takes the index of newly inserted node and the heap we're inserting
        self.shiftUp(len(self.heap) - 1, self.heap)

    def remove(self):
        # first we swap the root and the last value of the heap
        self.swap(0, len(self.heap) - 1, self.heap)

        # then we'll pop that swapped root value at the end of heap
        valueToRemove = self.heap.pop()

        # then we'll shiftDown the newly swapped root value to it's right position
        self.shiftDown(0, len(self.heap) - 1, self.heap)

        return valueToRemove

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


arr = [30, 12, 43, 54, 23, 4, 5, 41]

heap = MinHeap(arr)
print(arr)