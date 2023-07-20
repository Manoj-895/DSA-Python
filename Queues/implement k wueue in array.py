class Queuee:
    def __init__(self, n, s):
        self.arr = [0]*s
        self.front=[0]*n
        self.nxt = [0]*s
        self.rear=[0]*n

        for i in range(n):
            self.front[i]=-1
        for i in range(n):
            self.rear[i]=-1
        for i in range(s):
            self.nxt[i]=i+1
        self.nxt[s-1]=-1

        self.freespot = 0

    # Pushes 'X' into the Mth stack. Returns true if it gets pushed into the stack, and false otherwise.
    def push(self, x, m):
        if(self.freespot == -1):
            return -1
        index = self.freespot
        self.freespot = self.nxt[index]
        if(self.front[m-1]==-1):
            self.front[m-1] =index
            self.rear[m-1] =index
            self.nxt[index]=-1
        else:
            self.nxt[self.rear[m-1]] = index
            self.rear[m-1] = index
            self.nxt[index]=-1
        self.arr[index] = x

    # Pops top element from Mth Stack. Returns -1 if the stack is empty, otherwise returns the popped element.
    def pop(self, m):
        if(self.front[m-1]==-1):
            return -1
        index = self.front[m-1]
        self.front[m-1]= self.nxt[index]
        self.nxt[index]= self.freespot
        self.freespot = index
        self.arr[index] = 0
        
        
q=Queuee(2,5)
q.push(2,1)
q.push(3,1)
q.push(4,2)
q.push(5,1)
q.push(6,2)
q.pop(2)
q.pop(2)
q.push(10,2)
print(q.arr,q.nxt,q.front,q.rear)
q.push(20,2)
print(q.arr,q.nxt,q.front,q.rear)