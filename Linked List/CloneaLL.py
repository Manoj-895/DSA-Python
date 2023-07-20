#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    #Function to clone a linked list with next and random pointer.
    def insertAtTail(self,data):
        node = Node(data)
        if(self.cloneHead == None):
            self.cloneHead = node
            self.cloneTail = node
            return
        else:
            self.cloneTail.next = node
            self.cloneTail = node
            

    def copyList(self, head):
        self.cloneHead = None
        self.cloneTail = None
        current = head
        while(current):
            self.insertAtTail(current.data)
            current = current.next
        
        mapper = {}
        current = head
        temp2 = self.cloneHead
        while(current):
            mapper[current]=temp2
            current = current.next
            temp2 = temp2.next
        current = head
        temp2 = self.cloneHead
        while(current):
            if(current.arb == None):
                temp2.arb = None
            else:
                temp2.arb = mapper[current.arb]
            current= current.next
            temp2 = temp2.next
            
        return self.cloneHead


# Most optimized fucked up code
class Solution:
    #Function to clone a linked list with next and random pointer.
    def insertAtTail(self,data):
        node = Node(data)
        if(self.cloneHead == None):
            self.cloneHead = node
            self.cloneTail = node
        else:
            self.cloneTail.next = node
            self.cloneTail = node
            
    def copyList(self, head):
        current = head
        self.cloneHead = None
        self.cloneTail = None
        
        while(current):
            self.insertAtTail(current.data)
            current = current.next
        current = head    
        temp = self.cloneHead
        
        while(current):
            next1 = current.next
            current.next = temp
            next2 = temp.next
            temp.next = next1
            current = next1
            temp = next2
            
        current = head
        temp = self.cloneHead
        
        while(current):
            if(current.next != None):
                if(current.arb != None):
                    current.next.arb = current.arb.next
                else:
                    current.next.arb = None
            current = current.next.next
        current = head
        temp = self.cloneHead
        while(current.next != None):
            print(current.data)
            current = current.next
            # print(current.data,temp.data)
            # current.next = temp.next
            # current = current.next
            # if(current.next != None):
            #     temp.next = current.next
            #     temp = temp.next 
        
        return self.cloneHead
            
