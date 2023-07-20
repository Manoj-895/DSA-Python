import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        heapq.heapify(arr)
        cost = 0
        while(len(arr)>1):
            a = heapq.heappop(arr)
            b = heapq.heappop(arr)
            ans = a + b
            heapq.heappush(arr,ans)
            cost = cost + ans
            
        return cost