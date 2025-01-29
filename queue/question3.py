class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class QueueUsingLinkedList:
    def __init__(self):
        self.front = self.rear = None  

    def enqueue(self, x):
        new_node = Node(x)
        if self.rear is None: 
            self.front = self.rear = new_node
            return
        self.rear.next = new_node  
        self.rear = new_node

    def dequeue(self):
        if self.front is None:  
            return None
        data = self.front.data
        self.front = self.front.next  
        if self.front is None:  
        
            self.rear = None
        return data

    def is_empty(self):
        return self.front is None 


q = QueueUsingLinkedList()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  
print(q.dequeue())  
print(q.is_empty())  
