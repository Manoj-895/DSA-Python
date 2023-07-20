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
    
    def linketoSecond(self):
        current = self.head
        while(current.next):
            current = current.next
        current.next = self.head.next.next

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        listLinked =  ''
        while itr:
            print(itr.data)
            listLinked += str(itr.data) + "==>"
            itr = itr.next
        print(listLinked)
    
    def isLooped(self):
        current = self.head
        mapped = {}
        while current:
            try:
                if(mapped[current] == True):
                    current.next=None
                    print("looped present at",current.data) 
                    return
                    
            except:
                mapped[current]=True
            current=current.next 
        print("not looped")

    def FloyedCycleDetection(self):
        slow = self.head
        fast = self.head.next

        while(fast != None and slow!= None):
            fast = fast.next
            if(fast != None):
                fast = fast.next
            slow = slow.next
            if(fast == slow):
                print("looped")
                return slow.next
        return False

    def getloopforFloyed(self):
        slow = self.head
        intersection = self.FloyedCycleDetection()
        if not (intersection):
            print("not looped")
            return
        while(slow != intersection):
            
            slow = slow.next
            intersection = intersection.next
        
        print(slow.data)
        

if __name__ == '__main__':
    li2=LinkedList()
    li = LinkedList()
    li.insert_values([5,10,20,30,50,55])
    li2.insert_at_end(5)
    li2.insert_at_end(4)
    li2.insert_at_end(3)
    li2.insert_at_end(1)
    # li2.linketoSecond()
    li.linketoSecond()
    # li.isLooped()
    # li.FloyedCycleDetection()
    li.getloopforFloyed()
    # li2.print()

    

    