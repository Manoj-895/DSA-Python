import heapq
# Standard templete library in python for heep is min heap
# so for max heap apploading as -1 values
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        heap = []
        for i in range(k):
            heapq.heappush(heap ,-1 *arr[i])
        for i in range(k , r+1):
            if(arr[i] < -1*(heap[0])):
                heapq.heappop(heap)
                heapq.heappush(heap , -1*arr[i])
        ans = heap[0]
        return -1*(ans)