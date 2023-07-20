class Node:
    def __init__(self,data,next) -> None:
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

    def removeDuplicatesSorted(self):
        current = self.head
        while(current):
            if(current.next != None and current.data == current.next.data):
                current.next = current.next.next
            else:
                current = current.next
            # start = current
            # while(start.next != None and start.data == start.next.data):
            #     start = start.next
            # current.next = start.next
            # current = current.next
    
    def unsortedDuplicates(self):
        current = self.head
        while(current):
            temp = current.next
            pre = current
            while(temp):
                if(current.data == temp.data):
                    pre.next = temp.next
                else:
                    pre=pre.next
                temp = temp.next
            current=current.next



if __name__ == '__main__':
    li=LinkedList()
    li2 = LinkedList()
    li2.insert_values([1,1,1,2,2,3,3,4,4,4,4,5,6])
    li2.removeDuplicatesSorted()
    li2.print()
    li.insert_values([4,2,0,4,4,5,1,1,4,0,5,1,1,0])
    li.unsortedDuplicates()
    li.print()
    