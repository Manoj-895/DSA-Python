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

    def getMiddle(self, head):
        if (head == None):
            return head
  
        slow = head
        fast = head
  
        while (fast.next != None and 
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
              
        return slow
    def MergeSortedLL(self,a,b):
        result = None
          
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
              
        # pick either a or b and recur..
        if a.data <= b.data:
            result = a
            result.next = self.MergeSortedLL(a.next, b)

        else:
            result = b
            result.next = self.MergeSortedLL(a, b.next)
        return result
    
    def MergeSort(self,h):
        if(h == None or h.next == None):
            return h
        
        mid = self.getMiddle(h)
        nextTomid = mid.next
        mid.next = None

        left = self.MergeSort(h)
        right = self.MergeSort(nextTomid)

        result = self.MergeSortedLL(left , right)

        return result


if __name__ == '__main__':
    li=LinkedList()
    li.insert_values([5,6,2,1,0,3])
    result = li.MergeSort(li.head)
    li.print(result)
