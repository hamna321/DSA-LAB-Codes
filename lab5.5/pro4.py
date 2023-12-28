class Queue:
    def __init__(self, capacity):
        self.front = 0
        self.rear = capacity - 1
        self.size = 0
        self.capacity = capacity
        self.array = [0] * self.capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.isFull():
            return
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        self.size += 1
        print(f"{item} enqueued to queue")

    def dequeue(self):
        if self.isEmpty():
            return float('-inf')
        item = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def getFront(self):
        if self.isEmpty():
            return float('-inf')
        return self.array[self.front]

    def getRear(self):
        if self.isEmpty():
            return float('-inf')
        return self.array[self.rear]
if __name__ == "__main__":
    queue = Queue(1000)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    print(f"{queue.dequeue()} dequeued from queue\n")
    print("Front item is", queue.getFront())
    print("Rear item is", queue.getRear())
