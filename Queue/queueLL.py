class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.rear == None

    def enQueue(self, item):
        temp = Node(item)
        if self.rear is None:
            # this makes self.front and rear a node .... see the next comment
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def deQueue(self):
        temp = self.front
        # as self.front is a node it has its next pointer
        temp = temp.next
        if self.isEmpty is None:
            print("Queue is empty")
            return
        print("% s dequeued from queue" % str(self.front))
        self.front = temp

        if self.front is None:
            self.rear = None



q = Queue()
q.enQueue(10)
q.enQueue(20)
q.deQueue()
q.deQueue()
q.enQueue(30)
q.enQueue(40)
q.enQueue(50)
q.deQueue()
print("Queue Front " + str(q.front.data))
print("Queue Rear " + str(q.rear.data))