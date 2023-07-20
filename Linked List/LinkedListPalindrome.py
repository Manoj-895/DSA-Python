class Node:
    def __init__(self,data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
    
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

    def palindromeByarray(self):
        LLarray=[]
        current = self.head
        while(current):
            LLarray.append(current.data)
            current = current.next
        i=0
        j=len(LLarray)-1
        while(i<j):
            if(LLarray[i] != LLarray[j]):
                return False
            i+=1
            j-=1
        return True

    def plindromewithoutArrayLL(self):
        current = self.head
        slow  = current
        fast = current
        while(fast.next != None):
            fast=fast.next
            if(fast.next != None):
                fast=fast.next
            else:
                break
            slow = slow.next
        mid = slow
        current = mid.next
        pre = None
        while(current != None):
            forward = current.next
            current.next = pre
            pre = current
            current = forward
        second = pre
        first = self.head
        while(second!= None):
            if(first.data != second.data):
                return False
            second = second.next
            first=first.next
        return True


if __name__ == '__main__':
    li = LinkedList()
    li.insert_values([1,2,11,3,2,1])
    print(li.palindromeByarray())
    print(li.plindromewithoutArrayLL())
    # li.print()
