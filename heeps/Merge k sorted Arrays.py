from os import *
from sys import *
from collections import *
from math import *
import heapq
class Node:
    def __init__(self, data, i, j):
        self.data = data
        self.i= i 
        self.j = j
  
    def __lt__(self, nxt):
        return self.data < nxt.data

def mergeKSortedArrays(kArrays, k:int):
	heap = []
	heapq.heapify(heap)
	for i in range(k):
		temp = Node(kArrays[i][0] ,i,0)
		heapq.heappush(heap,temp)
	
	ans = []

	while(len(heap) > 0):
		temp = heap[0]
		ans.append(temp.data)
		heapq.heappop(heap)
		i = temp.i
		j = temp.j

		if(j+1 < len(kArrays[i])):
			temp1 = Node(kArrays[i][j+1] , i , j+1)
			heapq.heappush(heap , temp1)
	
	return ans

