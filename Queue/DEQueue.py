class Queue:
    def __init__(self, capacity):
        self.front = self.rear = -1
        self.capacity = capacity
        self.Q = [None]*self.capacity
        self.size = 0

    def isFull(self):
        if self.size == self.capacity:
            return True

    def isEmpty(self):
        if self.size == 0:
            return True

    def insertFromRear(self, item):
        if self.isFull():
            print("queue is FUll")
            return
        elif self.isEmpty():
            self.front += 1
            self.rear += 1
            self.Q[self.rear] = item
            self.size += 1
        else:
            self.rear += 1
            self.Q[self.rear] = item
            self.size += 1
        print("Enqueud to queue", item," at",self.rear)

    def deleteFromRear(self):
        if self.isEmpty():
            print("queue is empty")
            return
        del self.Q[self.rear]
        self.rear -= 1
        print("% s dequeued from queue" % str(self.Q[self.front]))

    def insertFromFront(self, item):
        if self.isFull():
            return
        if self.isEmpty():
            self.rear += 1
            self.front += 1
            self.Q[self.front] = item
            self.size += 1
            print("Enqueud to queue", item, "at", self.front)
            return
        elif self.front == 0:
            print("There is not space at the front")
        else :
            self.front -= 1
            self.Q[self.front] = item
            print("Enqueud from Front", item, "at", self.front)

    def deleteFromFront(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("% s dequeued from queue" % str(self.Q[self.front]))
            self.Q[self.front] = None
            self.front += 1

    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

        # Function to get rear of queue

    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])

q = Queue(4)
q.insertFromRear(30)
q.insertFromRear(40)
q.deleteFromFront()
q.insertFromFront(50)
q.insertFromFront(60)
q.insertFromRear(90)
q.insertFromFront(20)
q.que_rear()
q.que_front()

