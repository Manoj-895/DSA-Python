class Heap:
    def __init__(self) -> None:
        self.arr=[]
        self.size = -1

    def insert(self , val):
        self.size += 1
        self.arr.append(val)

        index = self.size
        while( index > 0):
            parent =  index //2

            if(self.arr[parent] < self.arr[index]):
                self.arr[parent] , self.arr[index] = self.arr[index] , self.arr[parent]
                index=parent
            else:
                return
        
    def deletHeap(self):
        if(self.size == 1):
            return -1
        self.arr[0] = self.arr[self.size]
        self.size -= 1
        self.arr.pop()
        index = 0
        
        self.hepefiy(index , self.size)

        # while(index < self.size):
        #     leftIndex = 2*index
        #     rightIndex = 2*index +1
        #     if(leftIndex < self.size and self.arr[index] < self.arr[leftIndex]):
        #         self.arr[index] , self.arr[leftIndex] = self.arr[leftIndex] , self.arr[index]
        #         index = leftIndex
        #     elif(rightIndex < self.size and self.arr[index] < self.arr[rightIndex]):
        #         self.arr[index] , self.arr[rightIndex] = self.arr[rightIndex] , self.arr[index]
        #         index = rightIndex
        #     else:
        #         return  
              
    def hepefiy(self , i ,size):
        largest = i
        leftindex = 2*i +1
        rightindex = 2*i +2

        if(leftindex < size and self.arr[largest] < self.arr[leftindex]):
            largest = leftindex
        if(rightindex < size and self.arr[largest] < self.arr [rightindex]):
            largest = rightindex

        if(largest != i):
            self.arr[largest],self.arr[i] = self.arr[i] , self.arr[largest]
            self.hepefiy(largest ,size)

    def sortHeap(self , n):
        size = n
        while(size > 1):
            self.arr[0] ,self.arr[size] = self.arr[size] ,self.arr[0]
            size -= 1
            self.hepefiy(0 , size)
            


a=Heap()
a.insert(10)
a.insert(20)
a.insert(90)
a.insert(33)
a.insert(5)
a.insert(8)
a.insert(4)
print(a.arr,"created heap")
a.deletHeap()
a.deletHeap()
print(a.arr,"heap after deletion")
b=Heap()
b.arr=[3,55,6,80,85]
b.size = 4
for i in range(b.size//2 , -1 ,-1):
    b.hepefiy(i , b.size)
print(b.arr , "created heap")
a.sortHeap(a.size)
print(a.arr,"sorted heap")





