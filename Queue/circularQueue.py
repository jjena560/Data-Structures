class CircularQ:
    def __init__(self, capacity):
        self.capacity = capacity
        self.Q = [None]*capacity
        self.front = self.rear = -1
        self.size = -1

    def isEmpty(self):
        if self.front == -1:
            return True
        return False

    def enQueue(self, item):
        if self.rear == self.capacity-1 and self.front != 0:
            self.rear = 0
            self.Q[self.rear] = item
            print("% s enqueued into queue" % str(self.Q[self.rear]))
            self.rear += 1

        elif self.isEmpty():
            self.front += 1
            self.rear += 1
            self.Q[self.rear] = item
            print("% s enqueued from queue" % str(self.Q[self.rear]))

        elif self.rear == self.capacity-1:
            print("Queue is Full")

        else:
            self.rear = (self.rear+1) % self.capacity
            self.Q[self.rear] = item
            print("% s enqueued into queue" % str(self.Q[self.rear]))
            self.size += 1

    def deQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
            
        #at last element
        elif self.front == self.rear:
            temp = self.Q[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            print("% s dequeued from queue" % str(self.Q[self.front]))
            temp = self.Q[self.front]
            self.front = (self.front + 1) % self.capacity
            return temp

queue = CircularQ(7)
queue.enQueue(10)
queue.enQueue(20)
queue.enQueue(30)
queue.enQueue(40)
queue.enQueue(50)
queue.enQueue(60)
queue.enQueue(70)
queue.deQueue()
queue.deQueue()

queue.enQueue(44)
queue.deQueue()
queue.enQueue(444)
queue.deQueue()