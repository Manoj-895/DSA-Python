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
    
    def MergeTwoSortesLL(self , other):
        first = self.head
        second = other
        
        if(first.data <= second.data):
            current1 = first
            next1 = current1.next
            current2 = second

            if(first.next == None):
                first.next = second
            while (next1 != None and current2 != None):
                if(current2.data >= current1.data and current2.data <= next1.data):
                    current1.next = current2
                    next2 = current2.next
                    current2.next = next1

                    current1 = current2
                    current2 = next2
                else:
                    current1 = next1
                    next1 = next1.next
                    if(next1 == None):
                        current1.next = current2
                        return first
            return first

if __name__ == '__main__':
    li = LinkedList()
    li.insert_values([1])
    li2 = LinkedList()
    li2.insert_values([2,5,8,9])
    # li2.print()
    data = li.MergeTwoSortesLL(li2.head)
    li.print(data)
    