class Solution():
    def mergeHeaps(self, a, b, n, m):
        #your code here
        arr = a+b
        def heapify(size , i):
            nonlocal arr
            largest = i
            left = 2*i+1
            right = 2*i+2
            if(left < size and arr[largest] < arr[left]):
                largest = left
            if( right  < size and arr[largest] < arr[right]):
                largest = right
            if(largest != i):
                arr[largest] , arr[i] = arr[i] , arr[largest]
                heapify(size , largest)
        
        size = n+m
        for i in range(size//2 , -1 , -1):
            heapify(size , i)
        return arr