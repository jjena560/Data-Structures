class Queue:
    def __init__(self, capacity):
        self.size = self.front = 0
        self.capacity = capacity
        self.rear = -1
        self.Q = [None]*self.capacity

    def isFull(self):
        if self.size == self.capacity:
            return True

    def isEmpty(self):
        if self.size == 0:
            return True

    def EnQueue(self, item):
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear = (self.rear+1)%self.capacity
            self.size += 1
            self.Q[self.rear] = item
            print("Enqueud to queue", item)

    def DeQueue(self):
        if self.isEmpty():
            print("QUEUE IS EMPTY")
            return
        else:
            print("% s dequeued from queue" % str(self.Q[self.front]))
            self.front = (self.front+1) % self.capacity
            self.size -= 1

    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

        # Function to get rear of queue

    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])





queue = Queue(30)
queue.EnQueue(10)
queue.EnQueue(20)
queue.EnQueue(30)
queue.EnQueue(40)
queue.DeQueue()
queue.que_front()
queue.que_rear()