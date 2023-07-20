class Node:
    def __init__(self,data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
        # self.head2 = None
        # self.tail = None
    
    def insert_at_beginning(self , data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if(self.head is None):
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    
    def insert_values(self,data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)
    
    def print(self,data=None):
        if self.head is None:
            print("linked list is empty")
            return
        if(data==None):
            itr = self.head
            
        else:
            itr = data
        listLinked =  ''
        while itr:
            listLinked += str(itr.data) + "==>"
            itr = itr.next
        print(listLinked)
    
    def createLl(self,data):
        if(self.head2 == None):
            self.head2 = Node(data=data)
            self.tail = self.head2
        else:
            self.tail.next = Node(data=data)
            self.tail = self.tail.next

    def reverse(self,node):
        pre = None
        current = node
        while(current):
            forward = current.next
            current.next = pre
            pre = current
            current = forward
        return pre

    def addTwoLL(self,other):
        first = self.head
        second = other
        carry = 0
        first = self.reverse(first)
        second = self.reverse(second)
        self.head2 = None
        self.tail=None

        while(first != None or second != None or carry != 0):
            val1 = 0
            val2 = 0
            if(first != None):
                val1 = first.data 
            if(second != None):
                val2 = second.data
            sum = val1 + val2 + carry
            digit = int(sum%10)
            self.createLl(digit)
            carry = int(sum/10)
            if(first != None):
                first=first.next
            if(second != None):
                second=second.next

        return self.reverse(self.head2)
                
if __name__ == '__main__':
    li1 = LinkedList()
    li2 = LinkedList()
    li1.insert_values([5,4,9])
    li2.insert_values([5,9,9])
    li1.print()
    li2.print()
    data = li1.addTwoLL(li2.head)
    li1.print(data)
