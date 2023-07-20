class Node:
    def __init__(self,pre=None,data=None,next=None) -> None:
        self.pre = pre
        self.data = data
        self.next = next

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append_at_end(self,data):
        if self.head == None:
            node  = Node(None,data,None)
            self.head = node
            return
        
        new_Node = Node(data=data)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_Node
        new_Node.pre = itr

    def prepend_at_Begining(self,data):
        if self.head == None:
            node  = Node(None,data,None)
            self.head = node
            return
        new_Node = Node(data=data)
        new_Node.next = self.head
        self.head = new_Node
    
    def get_length(self):
        count =0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        print(count)
        return(count)  


    def remove_at_end(self):
        itr = self.head
        len = self.get_length()
        count=0
        while itr.next:
            if count == len -2:
                break
            count +=1
            itr = itr.next
        itr.next = None
        

    def show(self):
        itr = self.head
        Doubly= ""
        while itr:
            Doubly = Doubly + str(itr.data) + "===>"
            itr=itr.next
        print(Doubly)


if __name__ == '__main__':
    dl=DoublyLinkedList()
    dl.prepend_at_Begining(90)
    dl.append_at_end(10)
    dl.append_at_end(20)
    dl.append_at_end(40)
    dl.prepend_at_Begining(55)
    dl.show()
    dl.remove_at_end()
    dl.show()
            

        