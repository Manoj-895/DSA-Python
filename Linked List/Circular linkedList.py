class Node:
    def __init__(self,data=None, next=None) -> None:
        self.data = data
        self.next = next

class CircularLinked:
    def __init__(self) -> None:
        self.head = None

    def insert_values(self,data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)
    
    def insert_at_beginning(self , data):
        itr = self.head
        while itr.next is not self.head:
            itr = itr.next
        node = Node(data,self.head)
        self.head = node
        itr.next = self.head
    
    def insert_at_end(self,data):
        if(self.head is None):
            self.head = Node(data=data)
            self.head.next = self.head
            return

        itr = self.head
        while itr.next is not self.head:
            itr = itr.next
        itr.next = Node(data,self.head)

    def get_length(self):
        count =0
        itr = self.head
        while True:
            count+=1
            if(itr.next is self.head):
                break
            itr = itr.next
        print(count)
        return(count)
    
    def add_at_index(self,data,index):
        if not(-1 < index < self.get_length()):
            raise Exception("invalid Index")

        if(index == 0):
            self.insert_at_beginning(data)
            return
        # automatic garbage collection in python so no need to delete the removed node
        itr = self.head
        count = 0
        while itr:
            if count == index-1 :
                itr.next=Node(data,itr.next)
                break
            count+=1
            itr = itr.next

    def ifCircularOrLinear(self):
        current = self.head
        firstNode = self.head
        while(current.next):
            if(current.next == firstNode):
                return "circular"
            current = current.next
        return "linear"

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        itr = self.head
        listLinked =  ''
        while True:
            listLinked += str(itr.data) + "==>"
            if(itr.next is self.head):
                break
            itr = itr.next
        itr=itr.next
        listLinked += str(itr.data)
        print(listLinked)
    

if __name__ == '__main__':
    li = CircularLinked()
    li.insert_values([5,10,20,30,50])
    li.print()
    li.get_length()
    # li.remove_at(3)
    li.add_at_index(99,4)
    li.insert_at_beginning(23)
    li.insert_at_end(59)
    # li.insert_after_value(20,22)
    # li.print()
    # li.remove_by_vlue(30)
    li.print()
    li.get_length()
    print(li.ifCircularOrLinear())