class DoublyDeque:
    def __init__(self, size):
        self.dq = [0 for i in range(size)]
        self.n = size
        self.front = -1
        self.rear = -1

    # Pushes 'X' in the front of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushFront(self, x):
        if(self.isFull() == True):
            # Deque is full.
            return False
        if(self.isEmpty() == True):
            # Deque is empty.
            self.front = self.rear = 0
        else:
            # Deque is NOT empty. So, decrement 'front' by 1.
            if (self.front == 0):
                self.front = self.n-1
            else:
                self.front -= 1

        # Insert the element at the front of deque.
        self.dq[self.front] = x
        return True

    # Pushes 'X' in the back of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushRear(self, x):
        if(self.isFull() == True):
            # Deque is full.
            return False
        if(self.isEmpty() == True):
            # Deque is empty.
            self.front = self.rear = 0
        else:
            # Deque is NOT empty. So, increment 'rear' by 1.
            if (self.rear == self.n-1):
                self.rear = 0
            else:
                self.rear += 1

        # Insert the element at the end of deque.
        self.dq[self.rear] = x
        return True

    # Pops an element from the front of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popFront(self):
        if(self.isEmpty() == True):
            # Deque is empty.
            return -1

        item = self.dq[self.front]

        if(self.front == self.rear):
            # Deque has only one element.
            self.front = self.rear = -1
        else:
            # Increment 'front' by 1.
            if (self.front == self.n-1):
                self.front = 0
            else:
                self.front += 1

        return item

    # Pops an element from the back of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popRear(self):
        if(self.isEmpty() == True):
            # Deque is empty.
            return -1

        item = self.dq[self.rear]

        if(self.front == self.rear):
            # Deque has only one element.
            self.front = self.rear = -1
        else:
            # Decrement 'rear' by 1.
            if (self.rear == 0):
                self.rear = self.n-1
            else:
                self.rear -= 1

        return item

    # Returns the first element of the deque. If the deque is empty, it returns -1.
    def getFront(self):
        if(self.isEmpty() == True):
            # Deque is empty.
            return -1
        return self.dq[self.front]

    # Returns the last element of the deque. If the deque is empty, it returns -1.
    def getRear(self):
        if(self.isEmpty() == True):
            # Deque is empty.
            return -1
        return self.dq[self.rear]

    # Returns true if the deque is empty. Otherwise returns false.
    def isEmpty(self):
        if(self.front == -1):
            return True
        return False

    # Returns true if the deque is full. Otherwise returns false.
    def isFull(self):
        if ((self.front == 0 and self.rear == self.n - 1) or (self.front == self.rear + 1)):
            return True
        return False
        

x = DoublyDeque(2)
x.popFront()
x.pushRear(29)
x.isEmpty()
x.getFront()
x.popRear()
x.pushFront(30)
x.popFront()
x.getRear()
x.isEmpty()
print(x.dq , x.rear , x.front)
x.pushRear(20)
print(x.dq)