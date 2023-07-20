class CircularQueue:
    def __init__(self, n):
        # Initialize your data structure.
        self.size = n
        # initializing queue with none
        self.queue = [None for i in range(n)]
        self.front = self.rear = -1

    # Enqueues 'X' into the queue. Returns true if it gets pushed into the queue, and false otherwise.
    def enqueue(self, value):
        # Write your code here
        if ((self.rear + 1) % self.size == self.front):
            return False
             
        # condition for empty queue
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
            return True
        else:
             
            # next position of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            return True



    # Dequeues pop element from queue. Returns -1 if the queue is empty, otherwise returns the popped element.
    def dequeue(self):
        # Write your code here.
        if (self.front == -1): # condition for empty queue
            return -1
            
        # condition for only one element
        elif (self.front == self.rear):
            temp=self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
        
if __name__ == '__main__':
    x = CircularQueue(5)
    print(x.enqueue(1))
    print(x.enqueue(2))
    print(x.enqueue(3))
    print(x.enqueue(4))
    print(x.enqueue(5))
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    