class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k  
        self.front = self.rear = -1  
        self.size = k

    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:  
            return False
        if self.front == -1:  
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = x
        return True

    def dequeue(self):
        if self.front == -1:  
            return -1
        data = self.queue[self.front]
        if self.front == self.rear:  
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data

    def front_element(self):
        return -1 if self.front == -1 else self.queue[self.front]

    def rear_element(self):
        return -1 if self.rear == -1 else self.queue[self.rear]


cq = CircularQueue(3)
print(cq.enqueue(1))  
print(cq.enqueue(2))  
print(cq.enqueue(3))  
print(cq.enqueue(4)) 
print(cq.dequeue())  
print(cq.front_element())  
print(cq.rear_element())  
