def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        shiftDown(0, endIdx - 1, array)

    return array


def buildMaxHeap(array):
    firstParentIndex = len(array) - 1 // 2

    for currentIdx in reversed(range(firstParentIndex)):
        shiftDown(currentIdx, len(array) - 1, array)

    print(array)


def swap(i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]


def shiftDown(currentIndex, endIndex, heap):
    childOneIndex = currentIndex * 2 + 1
    while childOneIndex <= endIndex:
        childTwoIndex = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1

        if childTwoIndex != -1 and heap[childTwoIndex] > heap[childOneIndex]:
            idxToSwap = childTwoIndex
        else:
            idxToSwap = childOneIndex

        if heap[idxToSwap] > heap[currentIndex]:
            swap(currentIndex, idxToSwap, heap)
            currentIndex = idxToSwap
            childOneIndex = currentIndex * 2 + 2

        else:
            break


array = [54, 6, 45, 24, 23, 10, 0]

print(heapSort(array))
