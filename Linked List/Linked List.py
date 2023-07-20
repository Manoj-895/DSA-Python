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

    def get_length(self):
        count =0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        print(count)
        return(count)   

    def remove_at(self,index):
        if not(0 < index < self.get_length()):
            raise Exception("invalid Index")

        if(index == 0):
            self.head = self.head.next
            return
        # automatic garbage collection in python so no need to delete the removed node
        itr = self.head
        count = 0
        while itr:
            if count == index-1 :
                itr.next = itr.next.next
                break
            count+=1
            itr = itr.next

    def add_at_index(self,data,index):
        if not(0 < index < self.get_length()):
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

    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after:
                self.add_at_index(data_to_insert,count+1)
            count+=1
            itr = itr.next

    def remove_by_vlue(self,data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
            count+=1
            itr = itr.next


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
    # li.insert_at_beginning(50)
    # li.insert_at_beginning(40)
    # li.insert_at_end(45)
    # li.insert_at_end(90)
    li.insert_values([5,10,20,30,50])
    li.print()
    li.get_length()
    # li.remove_at(3)
    li.add_at_index(99,2)
    li.insert_after_value(20,22)
    li.print()
    li.remove_by_vlue(30)
    li.print()