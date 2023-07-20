import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        heapq.heapify(arr)
        ans = 0
        while(len(arr) >1):
            a = arr[0]
            heapq.heappop(arr)
            b = arr[0]
            heapq.heappop(arr)
            c=a+b
            ans = ans+c
            heapq.heappush(arr,c)
        return ans