import heapq
import sys
class Node:
    def __init__(self, data, i, j):
        self.data = data
        self.i= i 
        self.j = j
  
    def __lt__(self, nxt):
        return self.data < nxt.data

def kSorted(a, k, n):
    heap = []
    heapq.heapify(heap)
    mini , maxi = sys.maxsize, -sys.maxsize - 1
    for i in range(k):
        temp = Node(a[i][0] ,i,0)
        heapq.heappush(heap,temp)
        maxi = max(maxi,temp.data)
        mini = min(mini , temp.data)
    
    start = mini
    end = maxi
    while(len(heap)>0):
        temper = heap[0]
        heapq.heappop(heap)

        mini = temper.data
        if(maxi - mini < end - start):
            start = mini
            end = maxi
        if(temper.j +1 < n):
            maxi = max(maxi ,a[temper.i][temper.j+1] )
            heapq.heappush(heap,Node(a[temper.i][temper.j+1],temper.i,temper.j+1))
        else:
            break
    return (end - start +1)

        

    

	