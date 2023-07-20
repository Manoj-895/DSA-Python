class Node:
    def __init__(self,data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
        
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

    def reverseLinkedList(self):
        pre = None
        current = self.head
        while(current != None):
            forword = current.next
            current.next = pre
            pre = current
            current = forword
        self.head = pre

    def reverseLLbyRecurssion(self,current,prev,num):
        if(num == 1):
            current=self.head
        if(current == None):
            self.head = prev
            return
        
        forword = current.next
        current.next = prev
        self.reverseLLbyRecurssion(forword,current,0)
        
    # def secondRecurssion(self):
    #     if(self.head == None):
    #         return self.head

    #     chotaHead = self.secondRecurssion()
    #     self.head.next.next = self.head
    #     self.head.next = None

    #     self.head =  chotaHead

    def ifCircularOrLinear(self):
        current = self.head
        firstNode = self.head
        while(current.next):
            if(current.next == firstNode):
                return "circular"
            current = current.next
        return "linear"
    
    def reverseBlock(self,head,k):
        if(head == None):
            return None
        next = None
        current=head
        pre = None
        count = 0
       
        while(count < k and current is not None):
            next = current.next
            current.next = pre
            pre = current
            current = next
            count+=1
        
        # print(head.data)
        if(next != None):
            head.next = self.reverseBlock(next,k)
        
        return  pre
        

    def middlewithFastandSlow(self):
        slow = self.head
        fast = self.head.next
        while(fast != None):
            fast = fast.next
            if(fast != None):
                fast = fast.next

            slow = slow.next

        return slow.data

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        listLinked =  ''
        while itr:
            listLinked += str(itr.data) + "==>"
            itr = itr.next
        print(listLinked)

if __name__ == '__main__':
    li = LinkedList()
    li.insert_values([5,10,20,30,50,60])
    # li.reverseLinkedList()
    # li.reverseLLbyRecurssion(None,None,1)
    # li.secondRecurssion()
    # print(li.middlewithFastandSlow())
    # li.head = li.reverseBlock(li.head,2)
    print(li.ifCircularOrLinear())
    li.print()