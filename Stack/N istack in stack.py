from os import *
from sys import *
from collections import *
from math import *

class NStack:
    def __init__(self, n, s):
        self.arr = [0]*s
        self.top=[0]*n
        self.nxt = [0]*s

        for i in range(n):
            self.top[i]=-1
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

        self.arr[index] = x

        self.nxt[index] = self.top[m-1]

        self.top[m-1] = index

        return True
        

    # Pops top element from Mth Stack. Returns -1 if the stack is empty, otherwise returns the popped element.
    def pop(self, m):

        if(self.top[m-1] == -1):
            return -1
        
        index = self.top[m-1]

        self.top[m-1] = self.nxt[index]

        self.nxt[index] = self.freespot

        self.freespot = index

        return self.arr[index]
        