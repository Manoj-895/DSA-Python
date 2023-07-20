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
    
    def Sort012s(self):
        zeros = 0
        ones = 0
        tows = 0
        temp = self.head
        while(temp != None):
            if(temp.data == 0):
                zeros+=1
            elif(temp.data == 1):
                ones+=1
            else:
                tows+=1
            temp=temp.next
        temp = self.head
        while(temp != None):
            if(zeros != 0):
                temp.data = 0
                zeros -=1
            elif(ones != 1):
                temp.data = 1
                ones -=1
            else:
                temp.data = 2
                tows -= 1
            temp=temp.next
        return self.head
    
    def Sort012sApproach2(self):
        zeroHead = Node(-1)
        zeroTail = zeroHead
        oneHead = Node(-1)
        onetail = oneHead
        twohead = Node(-1)
        twotail = twohead

        current = self.head
        while(current):
            if(current.data == 0):
                zeroTail.next = current
                zeroTail = current
            elif(current.data == 1):
                onetail.next = current
                onetail = current
            elif(current.data == 2):
                twotail.next = current
                twotail = current
            current=current.next
        
        if(oneHead.next != None):
            zeroTail.next = oneHead.next
            onetail.next = twohead.next
        else:
            zeroTail.next = twohead.next
        
        head =  zeroHead.next
        return head
                

    def print(self,data=None):
        if self.head is None:
            print("linked list is empty")
            return
        if(data!=None):
            itr = self.head
        else:
            itr = data
        listLinked =  ''
        while itr:
            listLinked += str(itr.data) + "==>"
            itr = itr.next
        print(listLinked)
    

if __name__ == '__main__':
    li = LinkedList()
    li.insert_values([0,1,1,0,0,1,2,2,1,2])
    # data = li.Sort012s()
    data = li.Sort012sApproach2()
    li.print(data)
